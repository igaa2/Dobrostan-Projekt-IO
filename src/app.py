from loguru import logger
import streamlit as st

from src.utils.data_classes import Variable, SessionStatePrefix, DataParams
from src.utils.utils import get_project_root, load_yaml
from src.streamlit.configuration_utils import (
    configurate_page,
    configure_sidebar,
    configurate_main,
    ensure_session_state,
    generate_sliders_and_toggles_for_variables,
    reset_session_state_by_prefix,
    warn_if_all_sliders_zero,
)
from src.streamlit.data_utils import (
    fetch_most_recent_year_data_for_variables,
    normalize_per_variable,
    validate_and_extract_validation,
)
from src.streamlit.plots import (
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
    config = load_yaml(root / "config.yaml")

    data_params = DataParams.from_dict(config["data"]["params"])
    variables = [Variable.from_dict(dictionary=d) for d in config["data"]["variables"]]
    logger.info(
        f"Number of variables used: {len(variables)}. "
        f"Id of variables used: {[v.variable_id for v in variables]}. "
    )

    # ==================== POBRANIE DANYCH ====================

    df_oryginal = fetch_most_recent_year_data_for_variables(
        variables=variables,
        params=data_params,
        sleep_between_requests=0.5,
    )

    validation_infos, validation_cv = validate_and_extract_validation(df=df_oryginal)

    df_normalized = normalize_per_variable(df=df_oryginal)

    # ==================== KONFIGURACJA STRONY ====================

    configurate_page()