The Cybersecurity Requirements for Telematics Systems matrix of requirements was developed in collaboration with motor freight carriers, telematics service providers, and cybersecurity experts.

![NMFTA Logo](https://raw.githubusercontent.com/nmfta-repo/nmfta-telematics_security_requirements/master/media/image1.png)

This repository hosts a *Telematics Cybersecurity Requirements Matrix*; all documents are licensed under the [Creative Commons `BY-NC-ND` 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/):

The current development version [![Requirements Publish](https://github.com/nmfta-repo/nmfta-telematics_security_requirements/actions/workflows/publish.yml/badge.svg)](https://github.com/nmfta-repo/nmfta-telematics_security_requirements/actions/workflows/publish.yml):
* [is available to browse online](https://nmfta-repo.github.io/nmfta-telematics_security_requirements/)
* [is available in Requirements Interchange Format (ReqIF)](https://nmfta-repo.github.io/nmfta-telematics_security_requirements/output.reqif)
* [is available as supplier questionnaires in excel format](https://nmfta-repo.github.io/nmfta-telematics_security_requirements/tsrm_questionnaires.xlsx)

See 'Download' below or 'Releases' tab to the right to get the latest official release.

[![License: CC BY-NC-ND 4.0](https://licensebuttons.net/l/by-nc-nd/4.0/80x15.png)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

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

# About

The deployment of Telematics, FMIS and/or ELDs in motor vehicles is pervasive today. As with any Information System (IS), it is the owner/operator of that system who bears the responsibility for managing the security of that system. This includes security of the information being collected, managed and stored, but also the security of the assets being monitored which – if not considered in procurement – could have their security posture worsened by the introduction of a Telematics, FMIS and/or ELD. In the case of agencies as the owners of an IS, their responsibility is detailed in the Federal Information Security Management Act of 2014[^1].

A core objective of this document is to provide information to owners of Telematics, FMIS and/or ELDs in the phases of procurement of these systems so they can manage risks to security. An additional objective is to provide comprehensive cybersecurity requirements that can be consulted by the owner and potential vendors to provide sufficient information that can prioritize the needs for cybersecurity in the Telematics, FMIS and/or ELD and validate the presence of the controls upon delivery of the system.

The approach taken to create this list included consultations with many authoritative sources of cybersecurity controls and then mapping them to the components of a Telematics, FMIS and/or ELD. To do this, the report considers a simplified model of a Telematics, FMIS and/or ELD. The four components of such a simplified system are broken down by *Vehicle Connection*, *Connectivity/Communications*, *Mobile App*, and *Cloud or Back-end* and are depicted in the figure below:

![Telematics systems diagram with labels](https://raw.githubusercontent.com/nmfta-repo/nmfta-telematics_security_requirements/master/media/telematics-diagram.png)

The Cybersecurity Requirements for Telematics Systems matrix uses the following terms for the components of a Telematics, FMIS and/or ELD:

-   *Vehicle Connection Device* – The component of Telematics, FMIS and/or ELD that is connected to vehicle networks -- tractor and/or trailer. There may also be a Human Machine Interface (HMI) aspect to this component. In cases where the HMI is a separate device from that which connects to vehicular networks, then all the requirements identified as being applicable to the ‘Mobile App’ (see below) should be considered to apply to the HMI device.

-   *Connectivity/Communications* – The component of a Telematics, FMIS and/or ELD which communicates data with the *Cloud or Back-end* (see below). This may or may not be the same device as the *Vehicle Connection Device*. In cases where they are the same device, both sets of the requirements identified as being applicable to a *Vehicle Connection Device* and the requirements identified as being applicable to *Connectivity/Communications* components should be considered to apply to the device.

-   *Cloud or Back-end* – The component or components of a Telematics, FMIS and/or ELD which are internet facing, where data is collected, where commands or remote control of vehicular components are possible and where monitoring of the entire fleet or subsets thereof is made possible by dashboard or operations center features. In some cases, these components will be hosted by service providers, while in others they may be hosted by the owner. In either case, all the requirements identified as being applicable to *Cloud or Back-end* should be considered to apply to the device.

-   *Mobile App* – The component of a Telematics, FMIS and/or ELD, which presents Human Machine Interfaces to drivers or other users of the system, may or may not have its own communications paths to the *Cloud or Back-end* and may or may not be hosted in a device separate from the *Vehicle Connection Device,* but is otherwise able to connect to and communicate with that vehicular component.

A goal of the working group was to ensure that stakeholders who procure equipment could also be capable of verifying that the equipment satisfies cybersecurity requirements. Therefore, each requirement includes a validation step which is intended to be executed by the purchaser. In some cases, the verification of the cybersecurity requirement requires more specialized knowledge than is reasonable to expect the purchaser to have. In these few cases, the validation steps recommend consulting a 3rd party report.

In recognizing that implementing cybersecurity for systems is an ongoing process for which there are rarely enough resources, each requirement has been each assigned a ‘criticality.’ These criticalities can be used to prioritize implementation by vendors or selection of vendors by purchasers.

We have avoided any requirements that are novel or otherwise unique in favor of referencing publicly available authoritative sources; at the time of drafting this report the authoritative references include:

1.	National Institute of Standards and Technology, Computer Security Resource Center. “Federal Information Security Modernization Act (FISMA).” Last modified December 2014. Accessed February 2020. http://csrc.nist.gov/drivers/documents/FISMA-final.pdf

2.	National Institute of Standards and Technology, Computer Security Resource Center. “Security and Privacy Controls for Information Systems and Organizations.” Last modified December 2020. Accessed May 2021. https://doi.org/10.6028/NIST.SP.800-53r5

3.	CTIA Certification LLC. “Cybersecurity Certification Test Plan for IoT Devices.” (CCTPID) Last modified January 2021. Accessed June 2021. https://ctiacertification.org/wp-content/uploads/2020/10/CTIA-Cybersecurity-Test-Plan-1.2.2.pdf

4.	ETSI Technical Committee Cyber Security (TC CYBER). “EN 303 645.” Last modified April 2020. Accessed May 2021. https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.00_30/en_303645v020100v.pdf 

5.	Cloud Security Alliance. “Consensus Assessment Initiative Questionnaire (CAIQ).” Last modified September 2019. Accessed May 2021. https://cloudsecurityalliance.org/artifacts/consensus-assessments-initiative-questionnaire-v3-1 

6.	Open Web Application Security Project (OWASP). “Application Security Verification Standard (ASVS).” Last modified March 2019. Accessed June 2019. https://github.com/OWASP/ASVS/raw/master/4.0/OWASP%20Application%20Security%20Verification%20Standard%204.0-en.pdf

7.	Cyber ITL. “Methodology.” Accessed June 2019. https://cyber-itl.org/about/methodology/

8.	ISO/IEC. “29147:2018 Information technology – Security techniques – Vulnerability disclosure.” Last modified Oct 2018. Accessed June 2019. https://www.iso.org/standard/72311.html

9.	Elazari, Amit. “#LegalBugBounty Hall of Fame.” Accessed June 2019. https://amitelazari.com/%23legalbugbounty-hof

10.	The Building Security In Maturity Model. “BSIMM.” Accessed June 2019. https://www.bsimm.com/download.html

11.	Open Web Application Security Project (OWASP). “Mobile Application Security Verification Standard (MASVS).” Accessed June 2019. https://github.com/OWASP/owasp-masvs/releases/tag/1.2RC

12.	Klinedinst, D. CMU, US DOT, FMCSA Office of Analysis, Research and Technology et. al. . “Cybersecurity Best Practices for Integration/Retrofit of Telematics and Aftermarket Electronic Systems into Heavy Vehicles.” Lost modified May 11th 2020. Accessed May 12th 2020. https://rosap.ntl.bts.gov/view/dot/49248

13. DHS, Binding Operational Directive 20-01. Last modified September 2, 2020. Accessed Jan 18th 2021. https://cyber.dhs.gov/bod/20-01/

14. Open Web Application Security Project (OWASP). “Embedded Application Security Project.” Last modified September 2020. Accessed May 2021. https://owasp.org/www-project-embedded-application-security/ 

Additional authoritative sources will be included in future versions of this report.

With regards to the FMCSA report "Cybersecurity Best Practices for Integration/Retrofit of Telematics and Aftermarket Electronic Systems into Heavy Vehicles" reference which is included in the references: the Cybersecurity Requirements for Telematics Systems Requirements matrix is aligned with the guidelines recommended by the FMCSA in their report. However, there are some differences between the audiences of the FMCSA report and the Cybersecurity Requirements for Telematics Systems Requirements matrix and also some requirements in the matrix which do not have a corresponding guideline in the FMCSA report. For more details on these topics please see [the NMFTA bulletin on the FMCSA "Cybersecurity Best Practices for Integration/Retrofit of Telematics and Aftermarket Electronic Systems into Heavy Vehicles."](http://www.nmfta.org/documents/hvcs/NMFTA%20Bulletin%20on%20FMCSA%20Heavy%20Vehicles%20Telematics%20Cybersecurity%20Best%20Practices%20v1.0.pdf?v=1)

# Cybersecurity Requirements for Telematics Systems Requirements Matrix Description

Each requirement captured is augmented with *Criticality*, *Verification Steps*, *Public Requirements References,* etc. A sample requirement is shown below:

![Telematics systems diagram with labels](https://raw.githubusercontent.com/nmfta-repo/nmfta-telematics_security_requirements/master/media/sample_requirement.png)

The example requirement above demonstrates the form in which each requirement is presented in Appendix A.

> ***Ref \#***

shows a unique value assigned to the requirement for easy reference


> ***Category***

groups like requirements together


> ***Criticality***

assigns a ‘priority’: a recommendation to the purchaser for each requirement:

-   ***High***: the working group advises that purchasers do not accept proposals that do not meet all ‘High’ criticality requirements

-   ***Medium***: the working group advises that purchasers may accept proposals that do not meet ‘Medium’ criticality requirements when the failure is justifiable or mitigated by the vendor

-   ***Low***: the working group advises that purchasers may accept proposals that do not meet ‘Low’ criticality requirements


> ***Applicable Component Categories***

shows to which of the components of the Telematics, FMIS and/or ELD that this requirement applies.


> ***Public Requirements References / Descriptions***

shows as many external authoritative requirements as were known to the working group at the time of this draft. These references are included so that

-   Purchasers can easily refer to the referenced sections of the document for further clarification on what are acceptable norms when evaluating vendor responses to RFPs AND

-   Vendors can use the referenced sections of the documents for establishing common language and terms in the responses to RFPs to amortize the costs of developing detailed responses.


> ***Requirement***

shows the requirement as it applies to the components of a Telematics, FMIS and/or ELD. The working group made every effort to make these requirements shorter and more succinct than the authoritative external references.


> ***Verification***

shows the steps which can be executed by purchasers to confirm that a given Telematics, FMIS and/or ELD satisfies this requirement. There are several cases where the working group does not expect that purchasers will perform their own verification. Where it is recommended that either a third party be engaged to provide an analysis which can be used by the purchasers to verify vendor claims, or that the vendor perform a demonstration that the requirement is satisfied which can be observed and confirmed by the purchaser. In such cases, rationale will be given. Due to the costly nature of delegating to a third party or of preparing a demonstration, this will only be recommended in cases where the requirement has been listed as having high *Criticality*. Because of the high *Criticality* of these requirements, it would be ideal to verify them relying on both a third party and a demonstration; the recommendation of the working group is that one or the other is sufficient.

-   In the context of verification via reports from a third party it is acceptable to either, as a purchaser, contract the third party for testing or to verify documentation provided by a third party contracted by the vendor.

-   In the context of demonstration by the vendor, it is important that the purchaser ensure the demonstration covers the non-functional aspects of these requirements, (e.g. for secure boot it is not sufficient to demonstrate that valid images are bootable, but rather it is necessary to demonstrate that tampered images are not bootable.)


> ***Remarks***

shows comments or notes from the working group.


# Questionnaire Description

This project also provides a set of questionnaires, one for each of *Vehicle Connection*, *Connectivity/Communications*, *Mobile App*, and *Cloud or Back-end*. These questionnaires can be sent in request to vendors to evaluate each of the applicable components of a telematics system that is being procured.

![Telematics systems diagram with labels](https://raw.githubusercontent.com/nmfta-repo/nmfta-telematics_security_requirements/master/media/sample_questionnaire.png)


# How to Make Contributions

NMFTA would like these requirements to be as useful as possible. We are open to refining them based on your feedback and/or changes which you would like to see made. However, the NMFTA does not want other custom versions of the requirements to be proliferated. This is the reason for the [Creative Commons `BY-NC-ND` 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) license of all the materials here.

The NMFTA will take your request for changes in whatever form is most convenient to you; an email or phone call is sufficient. GitHub issues and pull requests are welcomed also.


# Change History

## v1.6 (release candidate)

* migrated all requirements out of excel in `Telematics Cybersecurity Requirements Matrix.xlsx` and into [strictdoc](https://github.com/strictdoc-project/strictdoc/) format in `Telematics_Security_Requirements_Matrix.sdoc`
* automatic builds of html, Requirements Interchange Format (ReqIF) and supplier questionnaires added
* TODO changes from Jonathan Stines and colleagues at Samsara (thank you!) to add NIST 800-82 references c.f. https://github.com/nmfta-repo/vcr-experiment/pull/58

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