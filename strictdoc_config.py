from strictdoc.core.project_config import ProjectConfig


def create_config() -> ProjectConfig:
    return ProjectConfig(
        project_title="Cybersecurity requirements for telematics systems developed in collaboration with motor freight carriers, telematics service providers and cybersecurity experts.",
        include_doc_paths=[
            "*.sdoc",
        ],
        project_features=[],
    )
