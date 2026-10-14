from strictdoc.core.project_config import ProjectConfig, ProjectFeature


def create_config() -> ProjectConfig:
    return ProjectConfig(
        project_title="Cybersecurity requirements for telematics systems developed in collaboration with motor freight carriers, telematics service providers and cybersecurity experts.",
        include_doc_paths=[
            "*.sdoc",
        ],
        project_features=[
            ProjectFeature.TABLE_SCREEN,
            ProjectFeature.TRACEABILITY_SCREEN,
            ProjectFeature.DEEP_TRACEABILITY_SCREEN,
            ProjectFeature.SEARCH,
        ],
    )
