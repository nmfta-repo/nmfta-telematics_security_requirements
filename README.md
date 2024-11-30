The Cybersecurity Requirements for Telematics Systems matrix of requirements was developed in collaboration with motor freight carriers, telematics service providers, and cybersecurity experts.

![NMFTA Logo](https://raw.githubusercontent.com/nmfta-repo/nmfta-telematics_security_requirements/master/media/image1.png)

This repository hosts a *Telematics Cybersecurity Requirements Matrix*; all documents are licensed under the [Creative Commons `BY-NC-ND` 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/): [![License: CC BY-NC-ND 4.0](https://licensebuttons.net/l/by-nc-nd/4.0/80x15.png)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

The current development version [![Requirements Publish](https://github.com/nmfta-repo/nmfta-telematics_security_requirements/actions/workflows/publish.yml/badge.svg)](https://github.com/nmfta-repo/nmfta-telematics_security_requirements/actions/workflows/publish.yml):
* is available to browse online:
  * [as a interactive document](https://nmfta-repo.github.io/nmfta-telematics_security_requirements/nmfta-telematics_security_requirements/Telematics_Security_Requirements_Matrix.html)
  * [and as the more familiar table as well](https://nmfta-repo.github.io/nmfta-telematics_security_requirements/nmfta-telematics_security_requirements/Telematics_Security_Requirements_Matrix-TABLE.html#10-Appendix-A)
* [is available in Requirements Interchange Format (ReqIF)](https://nmfta-repo.github.io/nmfta-telematics_security_requirements/output.reqif)
* [is available as supplier questionnaires in excel format](https://nmfta-repo.github.io/nmfta-telematics_security_requirements/tsrm_questionnaires.xlsx)

See 'Download' below or 'Releases' tab to the right to get the latest official release.

This matrix of requirements was initially developed during the project to create templates for use by motor freight carriers in procuring telematics solutions ([github nmfta-repo/nmfta-rfp_templates](https://github.com/nmfta-repo/nmfta-rfp_templates)) and is now actively developed and hosted here in its own project.

THE INFORMATION CONTAINED HEREIN IS PROVIDED “AS IS” WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE INFORMATION IS WITH THE USER.

The purpose of this document is to provide government agency Fleet Managers and private industry stakeholders (e.g. TSPs, carriers, OEMs, Tier 1 suppliers, and others) responsible for the selection and procurement of Telematics, Fleet Management Information Systems (FMIS) and/or ELDs with situational awareness of potential cybersecurity risks of deploying such systems. This report also delivers a comprehensive list of cybersecurity requirements that should be satisfied by all components of a Telematics, Fleet Management Information System (FMIS) and/or Electronic Logging Devices (ELD), including validation steps for federal agencies and private industry stakeholders when deploying such systems.

# Contributors

This requirements matrix and the [Request For Proposal Contract Template Language project](https://github.com/nmfta-repo/nmfta-rfp_templates) where it was originally developed was made possible through the generous contributions of
thought leadership and technical expertise of many collaborators across the heavy vehicle cybersecurity community,
working to push the industry forward and make it more resilient. Though some of our contributors wish to remain
anonymous, we are deeply grateful to everyone who has given their time and energy to make this a reality.


| **Fleet Managers**   | **Telematics Providers** | **Independents**                                                |
|:--------------------:|:------------------------:|:---------------------------------------------------------------:|
|   Bill Brown, Retired Manager of Fleet Telematics, SEFL  | Derek Held, Zonar Systems| Altaz Valani, Security Compass                                  |
|                      | Geotab                   | Mr. Mark Zachos, President, DG Technologies                     |
|                      |                          | Richard M. Litwinczuk, Senior Cybersecurity Engineer, Land Cyber Mission Assurance Program DND |
|                      |                          | Jacob D'Aoust, Junior Researcher, DeepMicro Limited |

![SEFL](https://raw.githubusercontent.com/nmfta-repo/nmfta-telematics_security_requirements/master/media/SFL2c_300dpi-resized.jpg) ![Zonar Systems](https://raw.githubusercontent.com/nmfta-repo/nmfta-telematics_security_requirements/master/media/zonar-logo-RGB-750.png) ![Geotab](https://raw.githubusercontent.com/nmfta-repo/nmfta-telematics_security_requirements/master/media/geotab-logo_full-colour-rgb_resized.png) ![Security Compass](https://raw.githubusercontent.com/nmfta-repo/nmfta-telematics_security_requirements/master/media/securitycompass-logo-resized.jpg) ![DG Technologies](https://raw.githubusercontent.com/nmfta-repo/nmfta-telematics_security_requirements/master/media/dg-logo.png)

# Download

[Download the latest (v1.5) release of *Telematics Cybersecurity Requirements Matrix* here](https://github.com/nmfta-repo/nmfta-telematics_security_requirements/releases/download/v1.5/nmfta-telematics_security_requirements-v1.5.zip)

# How to Make Contributions

NMFTA would like these requirements to be as useful as possible. We are open to refining them based on your feedback and/or changes which you would like to see made. However, the NMFTA does not want other custom versions of the requirements to be proliferated. This is the reason for the [Creative Commons `BY-NC-ND` 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) license of all the materials here.

The NMFTA will take your request for changes in whatever form is most convenient to you; an email or phone call is sufficient. GitHub issues and pull requests are welcomed also.


# Change History

## v1.6 (release candidate)

* migrated all requirements out of excel in `Telematics Cybersecurity Requirements Matrix.xlsx` and into [strictdoc](https://github.com/strictdoc-project/strictdoc/) format in `Telematics_Security_Requirements_Matrix.sdoc`
* automatic builds of html, Requirements Interchange Format (ReqIF) and supplier questionnaires added
* changes from Jonathan Stines and colleagues at Samsara (thank you!) to add NIST 800-82 references c.f. https://github.com/nmfta-repo/vcr-experiment/pull/58

## v1.5 (2022 Feb)

* updated NIST 800-53 outward references to match r5 (of 800-53)
* corrected format of outward references to FMCSA document
* updated outward references to match TS 103 645 v1.1.1 revision of ETSI document
* updated outward references to newest CAIQ version
* added outward references to OWASP to 10
* added outward references to UL 1376
* added new requirements in response to gaps identified relative to UL 1376: SCP-140, CM-040, M-040, SCP-092, SII-041, and SAA-050


## v1.4 (2021 Mar)

* the wording and diagrams in the project are updated to clearly indicate that these requirements apply to trailer telematics and OEM telematics
* renamed 'security control' matrix column to 'category'
* added references to CISA BOD 20-01 to requirements for vulnerability disclosure programs


## v1.3 (2020 May)

* added new requirements to reflect the 'GDL' guidelines of the FMCSA report report, Cybersecurity Best Practices for Integration/Retrofit of Telematics and Aftermarket Electronic Systems into Heavy Vehicles and also added GDL references to existing matrix requirements where the GDLs were relevant. These changes were reviewed by the working group. See #8
* added new requirements to capture disposal of goods process requirements. This material was reviewed by the working group. See #10
* reformatted the 'Supplier Questionnaire' tab for better readability.
* added more introductory material to the README in order to better describe how to use the requirements and questionnaires.
* reformatted the 'Printable Matrix' tab to make it more suitable to include as an appendix when printed. Bigger font, more page breaks, headers and footers. See #9


## v1.2 (2019 Dec)

For this release, the Telematics Cybersecurity Requirements Matrix was extracted from release 1.1 of nmfta-repo/nmfta-rfp_templates. The v1.2 matches the contents of that release.
