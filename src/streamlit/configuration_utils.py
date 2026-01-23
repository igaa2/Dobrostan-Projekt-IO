import streamlit as st
from streamlit.delta_generator import DeltaGenerator
from loguru import logger
from src.utils.utils import get_project_root, load_md
from src.utils.data_classes import Variable, SessionStatePrefix


def configurate_page() -> None:
    """Set Streamlit page configuration."""
    st.set_page_config(
        page_title="Dobrostan Województw Polski",
        page_icon="📊",
        layout="wide",  # page elements use the entire screen width
        initial_sidebar_state="expanded",
        menu_items={"About": load_md(get_project_root() / "streamlit" / "about.md")},
    )
    logger.info("Streamlit page configured.")
