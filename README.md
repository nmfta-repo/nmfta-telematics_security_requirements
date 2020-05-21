The Cybersecurity Requirements for Telematics Systems matrix of requirements was developed in collaboration with motor freight carriers, telematics service providers, and cybersecurity experts.

![NMFTA Logo](https://raw.githubusercontent.com/nmfta-repo/nmfta-telematics_security_requirements/master/media/image1.png)

This repository hosts a *Telematics Cybersecurity Requirements Matrix*; all documents are licensed under the [Creative Commons `BY-NC-ND` 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/):

[![License: CC BY-NC-ND 4.0](https://licensebuttons.net/l/by-nc-nd/4.0/80x15.png)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

This matrix of requirements was initially developed during the project to create templates for use by motor freight carriers in procuring telematics solutions ([github nmfta-repo/nmfta-rfp_templates](https://github.com/nmfta-repo/nmfta-rfp_templates)) and is now actively developed and hosted here in its own project.

The purpose of this document is to provide government agency Fleet Managers and private industry stakeholders (e.g. TSPs, carriers, OEMs, Tier 1 suppliers, and others) responsible for the selection and procurement of Telematics, Fleet Management Information Systems (FMIS) and/or ELDs with situational awareness of potential cybersecurity risks of deploying such systems. It delivers a comprehensive list of cybersecurity requirements which should be satisfied by all components of a Telematics, Fleet Management Information System (FMIS) and/or Electronic Logging Devices (ELD) and includes validation steps for those federal agencies and private industry stakeholders in deploying such systems as well as vendor questionnaires.

# Contributors

This requirements matrix and the [Request For Proposal Contract Template Language project](https://github.com/nmfta-repo/nmfta-rfp_templates) where it was originally developed was made possible through the generous contributions of
thought leadership and technical expertise of many collaborators across the heavy vehicle cybersecurity community,
working to push the industry forward and make it more resilient. Though some of our contributors wish to remain
anonymous, we are deeply grateful to everyone who has given their time and energy to make this a reality.


| **Fleet Managers**   | **Telematics Providers** | **Independents**                                                |
|:--------------------:|:------------------------:|:---------------------------------------------------------------:|
|                      | Derek Held, Zonar Systems| Altaz Valani, Security Compass                                  |
|                      | Geotab                   | Mr. Mark Zachos, President, DG Technologies                     |
|                      |                          | Richard M. Litwinczuk, Senior Cybersecurity Engineer, Land Cyber Mission Assurance Program DND |

![Zonar Systems](https://raw.githubusercontent.com/nmfta-repo/nmfta-telematics_security_requirements/master/media/zonar-logo-RGB-750.png) ![Geotab](https://raw.githubusercontent.com/nmfta-repo/nmfta-telematics_security_requirements/master/media/geotab-logo_full-colour-rgb_resized.png) ![Security Compass](https://raw.githubusercontent.com/nmfta-repo/nmfta-telematics_security_requirements/master/media/securitycompass-logo-resized.jpg) ![DG Technologies](https://raw.githubusercontent.com/nmfta-repo/nmfta-telematics_security_requirements/master/media/dg-logo.png)

# Download

[Download the latest (v1.3) release of *Telematics Cybersecurity Requirements Matrix* here](https://github.com/nmfta-repo/nmfta-telematics_security_requirements/releases/download/v1.3/nmfta-telematics_security_requirements-v1.3.zip)

# About

The deployment of Telematics, FMIS and/or ELDs is pervasive today. As with any Information System (IS), it is the owner/operator of that system who bears the responsibility for managing the security of that system. This includes security of the information being collected, managed and stored, but also the security of the assets being monitored which – if not considered in procurement – could have their security posture worsened by the introduction of a Telematics, FMIS and/or ELD. In the case of agencies as the owners of an IS, their responsibility is detailed in the Federal Information Security Management Act of 2014.

One of the core objectives of this document is to provide information to owners of Telematics, FMIS and/or ELDs in the phases of procurement of these systems so that they can manage the risks to security. Then also to provide them with comprehensive cybersecurity requirements that can be consulted by the owner and also the potential vendors and to provide the owners with sufficient information that they can prioritize the needs for cybersecurity in the Telematics, FMIS and/or ELD and also validate the presence of the controls upon delivery of the system.

The approach taken to create this list included consultations with many authoritative sources of cybersecurity controls and then mapping these to the components of a Telematics, FMIS and/or ELD. To do this the report considers a simplified model of a Telematics, FMIS and/or ELD. The four components of such a simplified system are broken down by *Physical In-cab*, *Connectivity/Communications*, *Mobile App*, and *Cloud or Back-end* and are depicted in the figure below:

![Telematics systems diagram with labels](https://raw.githubusercontent.com/nmfta-repo/nmfta-telematics_security_requirements/master/media/telematics-diagram.png)

The Cybersecurity Requirements for Telematics Systems matrix uses the following terms for the components of a Telematics, FMIS and/or ELD:

-   *Physical In-Cab Device* – The component of Telematics, FMIS and/or ELD that is connected to vehicle networks. There may also be a Human Machine Interface aspect to this component. In cases where the HMI is a separate device from that which connects to vehicular networks then all the requirements identified as being applicable to the ‘Mobile App’ (see below) should be considered to apply to the HMI device.

-   *Connectivity/Communications* – The component of a Telematics, FMIS and/or ELD which communicates data with the *Cloud or Back-end* (see below). This may or may not be the same device as the *Physical In-Cab Device*. In cases where they are the same device then both sets of all the requirements identified as being applicable to a *Physical In-Cab Device* and all the requirements identified as being applicable to *Connectivity/Communications* components should be considered to apply to the device.

-   *Cloud or Back-end* – The component or components of a Telematics, FMIS and/or ELD which are ‘internet facing’, where data is collected, where commands or remote control of vehicular components are possible and where monitoring of the entire fleet or subsets thereof is made possible by dashboard or ‘operations center’ features. In some cases, these components will be hosted by service providers, while in others they may be hosted by the owner. In either case, all the requirements identified as being applicable to *Cloud or Back-end* should be considered to apply to the device.

-   *Mobile App* – The component of a Telematics, FMIS and/or ELD which presents Human Machine Interfaces to drivers or other users of the system, has its own communications paths to the *Cloud or Back-end* and may or may not be hosted in a device separate from the *Physical In-Cab Device* but is otherwise able to connect to and communicate with that ‘vehicular’ component.

A goal of the working group was to ensure that the stakeholders that procure the equipment could also be capable of verifying that the equipment satisfies the cybersecurity requirements; therefore, each requirement includes a validation step which is intended to be executed by the purchaser. In some cases, the verification of the cybersecurity requirement requires more specialized knowledge than is reasonable to expect the purchaser to have. In these cases, the validation steps recommend consulting a 3^rd^ party report; but these cases are in the minority.

Furthermore, in recognition of the fact that the implementing cybersecurity for systems is an ongoing process for which there rarely is enough resources, the requirements have been each assigned a ‘criticality.’ These criticalities can be used to prioritize implementation by vendors or selection of vendors by purchasers.

Whereas the Cybersecurity Requirements for Telematics Systems matrix does include a comprehensive list of cybersecurity requirements as they apply to the components of a Telematics, FMIS and/or ELDs, it does not contain any requirements which are novel or otherwise defined uniquely by this report. i.e. all requirements are referenced to the prior, authoritative sources.

There are multiple authoritative sources to which the report could refer in the effort to include outward references for all of the cybersecurity requirements; at the time of drafting this report the authoritative references include:

1.	National Institute of Standards and Technology, Computer Security Resource Center. “Federal Information Security Modernization Act (FISMA).” Last modified December 2014. Accessed February 2020. http://csrc.nist.gov/drivers/documents/FISMA-final.pdf

2.	National Institute of Standards and Technology, Computer Security Resource Center. “Security and Privacy Controls for Federal Information Systems and Organizations.” Last modified January 2015. Accessed June 2019. https://doi.org/10.6028/NIST.SP.800-53r4  

3.	CTIA Certification LLC. “IoT Cybersecurity Certification Test Plan.” (ITCCTP) Last modified May 2019. Accessed June 2019. https://api.ctia.org/wp-content/uploads/2019/05/ctia_IoT_cybersecurity_pmd_ver-1_1.pdf 

4.	ETSI Technical Committee on Cybersecurity (TC CYBER). “TS 103 645.” Last modified February 2019. Accessed June 2019. https://www.etsi.org/deliver/etsi_ts/103600_103699/103645/01.01.01_60/ts_103645v010101p.pdf

5.	Cloud Security Alliance. “Consensus Assessment Initiative Questionnaire (CAIQ).” Last modified September 2019. Accessed June 2019. https://cloudsecurityalliance.org/artifacts/consensus-assessments-initiative-questionnaire-v3-0-1/

6.	Open Web Application Security Project (OWASP). “Application Security Verification Standard (ASVS).” Last modified March 2019. Accessed June 2019. https://github.com/OWASP/ASVS/raw/master/4.0/OWASP%20Application%20Security%20Verification%20Standard%204.0-en.pdf 

7.	Cyber ITL. “Methodology.” Accessed June 2019. https://cyber-itl.org/about/methodology/

8.	ISO/IEC. “29147:2018 Information technology – Security techniques – Vulnerability disclosure.” Last modified Oct 2018. Accessed June 2019. https://www.iso.org/standard/72311.html 

9.	Elazari, Amit. “#LegalBugBounty Hall of Fame.” Accessed June 2019. https://amitelazari.com/%23legalbugbounty-hof 

10.	The Building Security In Maturity Model. “BSIMM.” Accessed June 2019. https://www.bsimm.com/download.html 

11.	Open Web Application Security Project (OWASP). “Mobile Application Security Verification Standard (MASVS).” Accessed June 2019. https://github.com/OWASP/owasp-masvs/releases/tag/1.2RC

12.	Klinedinst, D. CMU, US DOT, FMCSA Office of Analysis, Research and Technology et. al. . “Cybersecurity Best Practices for Integration/Retrofit of Telematics and Aftermarket Electronic Systems into Heavy Vehicles.” Lost modified May 11th 2020. Accessed May 12th 2020. https://rosap.ntl.bts.gov/view/dot/49248

It is almost certainly true that there are other authoritative sources not included in the present references and expect future refinements of the requirements to include the addition of more references.

# Cybersecurity Requirements for Telematics Systems Requirements Matrix Description

Each requirement captured is augmented with *Criticality*, *Verification Steps*, *Public Requirements References* etc. Please consider the example requirement below:

![Telematics systems diagram with labels](https://raw.githubusercontent.com/nmfta-repo/nmfta-telematics_security_requirements/master/media/sample_requirement.png)

The example requirement above demonstrates the form in which each requirement is presented in Appendix A.

> ***Ref \#***

shows a unique value assigned to the requirement for easy reference


> ***Security Controls***

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

This project also provides a set of questionnaires, one for each of *Physical In-cab*, *Connectivity/Communications*, *Mobile App*, and *Cloud or Back-end*. These questionnaires can be sent in request to vendors to evaluate each of the applicable components of a telematics system that is being procured.

![Telematics systems diagram with labels](https://raw.githubusercontent.com/nmfta-repo/nmfta-telematics_security_requirements/master/media/sample_questionnaire.png)


# How to Make Contributions

NMFTA would like these requirements to be as useful as possible. We are open to refining them based on your feedback and/or changes which you would like to see made. However, the NMFTA does not want other custom versions of the requirements to be proliferated. This is the reason for the [Creative Commons `BY-NC-ND` 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) license of all the materials here.

The NMFTA will take your request for changes in whatever form is most convenient to you; an email or phone call is sufficient. Github issues and pull requests are welcomed also.
