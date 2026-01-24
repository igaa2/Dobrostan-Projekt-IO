from loguru import logger
import streamlit as st

from src.utils.data_classes import Variable, SessionStatePrefix, DataParams
from src.utils.utils import get_project_root, load_yaml
from src.dashboard.configuration_utils import (
    configurate_page,
    configure_sidebar,
    configurate_main,
    ensure_session_state,
    generate_sliders_and_toggles_for_variables,
    reset_session_state_by_prefix,
    warn_if_all_sliders_zero,
)
from src.dashboard.data_utils import (
    fetch_most_recent_year_data_for_variables,
    normalize_per_variable,
    validate_and_extract_validation,
)
from src.dashboard.plots import (
    create_map,
    create_horizontal_barplot_with_mean_line,
    create_radar,
)
from src.composite_index.validator import VariableValidator
from src.composite_index.copras import (
    calculate_copras,
    calculate_hybrid_weights,
)


def main():
    root = get_project_root()
    config = load_yaml(root / "src" / "config.yaml")

    data_params = DataParams.from_dict(config["data"]["params"])
    variables = [Variable.from_dict(dictionary=d) for d in config["data"]["variables"]]
    logger.info(
        f"Number of variables used: {len(variables)}. "
        f"Id of variables used: {[v.variable_id for v in variables]}. "
    )

    # ==================== POBRANIE DANYCH ====================

    with st.spinner("Pobieranie danych z Banku Danych Lokalnych GUS..."):
        df_oryginal = fetch_most_recent_year_data_for_variables(
            variables=variables,
            params=data_params,
            sleep_between_requests=0.5,
        )

    validation_infos, validation_cv = validate_and_extract_validation(df=df_oryginal)

    df_normalized = normalize_per_variable(df=df_oryginal)

    # ==================== KONFIGURACJA STRONY ====================

    configurate_page()

    hide_warning_style = """
        <style>
            .stAlert {display:none;}
        </style>
    """
    st.markdown(hide_warning_style, unsafe_allow_html=True)

    # ==================== KONFIGURACJA PANELU BOCZNEGO ====================

    configure_sidebar()

    ensure_session_state(variables=variables)
    generate_sliders_and_toggles_for_variables(
        variables=variables, validation=validation_infos
    )

    if warn_if_all_sliders_zero():
        st.stop()

    # Przyciski resetów
    col_reset_sliders, col_reset_toggles = st.sidebar.columns(2)

    with col_reset_sliders:
        if st.button(
            f"🔄⚖️ Resetuj {SessionStatePrefix.SLIDER.value}",
            use_container_width=True,
        ):
            reset_session_state_by_prefix(SessionStatePrefix.SLIDER.value)
            st.rerun()

    with col_reset_toggles:
        if st.button(
            f"🔄📉 Resetuj {SessionStatePrefix.TOGGLE.value}",
            use_container_width=True,
        ):
            reset_session_state_by_prefix(SessionStatePrefix.TOGGLE.value)
            st.rerun()

    # ==================== PRZELICZENIE WSKAŹNIKA ====================

    df_index = calculate_copras(
        df=df_normalized,
        weights=calculate_hybrid_weights(
            validation_cv=validation_cv,
            slider_weights=SessionStatePrefix.extract_sliders_keys(
                dictionary=st.session_state
            ),
        ),
        stimulants=SessionStatePrefix.extract_toggles_keys(dictionary=st.session_state),
    )

    # ==================== KONFIGURACJA PANELU GŁÓWNEGO ====================

    configurate_main()

    col_map, col_barplot = st.columns([2, 3])

    with col_map:
        fig_map = create_map(
            df=df_index,
            value_col_name="value",
            unit_col_name="unit_name",
            value_label="Wskaźnik dobrostanu",
        )
        st.plotly_chart(fig_map, width="stretch")

    with col_barplot:
        fig_barplot = create_horizontal_barplot_with_mean_line(
            df=df_index,
            value_col_name="value",
            value_label="Wskaźnik dobrostanu",
            unit_col_name="unit_name",
            unit_label="Województwo",
        )
        st.plotly_chart(fig_barplot, width="stretch")

    # Wybór województw do porównania
    st.subheader("Porównanie województw - dane po normalizacji wektorowej")

    multiselect_key = SessionStatePrefix.MULTISELECT.value
    if multiselect_key not in st.session_state:
        st.session_state[multiselect_key] = df_index["unit_name"].head(3).tolist()

    st.multiselect(
        "Wybierz województwa do porównania",
        options=df_index["unit_name"],
        default=st.session_state[multiselect_key],
        key=multiselect_key,
        placeholder="Nie wskazano ani jednego województwa.",
    )

    if st.session_state[multiselect_key]:
        fig_radar = create_radar(
            df=df_normalized,
            value_col_name="value",
            variable_id_col_name="variable_id",
            variable_col_name="name",
            unit_col_name="unit_name",
            chosen_units=st.session_state[multiselect_key],
            stimulants=SessionStatePrefix.extract_toggles_keys(
                dictionary=st.session_state
            ),
        )
        st.plotly_chart(fig_radar, width="stretch")
    else:
        st.warning("Wybierz przynajmniej jedno województwo.")


if __name__ == "__main__":
    main()
