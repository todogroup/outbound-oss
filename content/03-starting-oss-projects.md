# Starting open source projects

## Motivation

* Why to start own projects? Overview of different variants (attract community, transparency, foundation-based)

Launching a new OSS project is comparable to a product introduction and it is, at first hand, a software development project - there is no difference to an internal software development project concerning planning, budget, staffing, testing etc. - the only difference is that everything happens in the public area. Be aware that publicly available source code is the “business card” of the organization to the software  ecosystem, and it is also the “business card” of its maintainers.

When thinking about to start an own OSS project there are several phases you should consider:

![oss-projcet-process](../img/LaunchinOSSProject.PNG)

## Project life cycle

The life cycle of an open source project describes the stages in which the project evolves, from its conception to its retirement or end of life stage. Typically, a project originates to solve a specific problem. It may become obsolete either because the problem does not exist anymore or because other projects are better suited to solve the problem. The figure below shows the different stages an open source project may undergo.

![Typical lifecycle of an open source project](../img/OSS-lifecycle.png)

### Planning or Concept Phase

This is the starting point of every open source project. It can also be referred to as the “initiation phase”. Normally, at this stage, only an idea exists or a specific problem has been identified which requires solution. In this phase, the open source project typically has the following characteristics:

* The problem that the project intends to solve has been clearly defined
* There is either no source code available yet or the source code is only internally available. In the first case, the project only exists as idea; in the second case, the project may have been started as an company-internal project and has not been published yet
* Possibly, the idea has been already shared with the community to get feedback. However, note that sharing such ideas that have only been discussed company-internally requires approval in advance.

Before starting a project, it is reasonable to get answers to the key questions:

* Is it possible to join efforts with an existing open source project?
* Can we launch and maintain the project using the OSS model?
* What constitutes success? How do we measure it?
* Can we financially sponsor the project? Do we have an internal executive champion?
* Will the project be able to attract outside enterprise participation (from the start)?
* Is there enough external interest to form and grow a developer community?

(Source: [Linux Foundation](https://www.linuxfoundation.org/en/resources/open-source-guides/starting-an-open-source-project/))

In addition, the following aspects should be considered in the planning phase:

* What is the goal of the project and will it solve the problem?
* Are there enough resources not only to start, but to support the project in the long-term? (You also need to obtain and ensure sponsorship)
* An appropriate license must be selected. The license should support the project goal.
* The legal requirements for contributions must be decided (if, for example, contributors must sign a CLA or DCO). Maybe your company has a standard approach for that.
* Execute additional checks. For example:

  * Make sure, that all license obligations are fulfilled
  * Export control: Under certain circumstances it might be required that the project must have an [export control classification number (ECCN)](https://en.wikipedia.org/wiki/Export_control), for example.
  * Check that the publication is not in conflict with existing trademarks.

* The [checklist of the Linux Foundation](https://www.linuxfoundation.org/en/resources/open-source-guides/starting-an-open-source-project/#checklist) contains a comprehensive set of topics you might want to consider
* Does it make sense to donate the code to a vendor-neutral, non-profit organization (that is, an open source foundation), or retain some control by owning and running the project under the responsibility of your company? Note that this decision depends on the project and may also be taken later in the life cycle. Typically, a project first needs to be published and generate interest in the community before it is handed over to a third-party organization.
* Set up an open source project governance. It establishes how to contribute to or maintain a project.
* Determine the tools and infrastructure the project members will use
* Carry out a technical review

  * Ensure that all critical content is removed from the project before publishing it. For example:

    * Dependencies to non-public components
    * Internal comments, references to other internal code, and the like
    * Access tokens and the like

  * Ensure that the coding style is consistent

* Where will the code be published? Typically, it will be in a company-owned organization on a code hosting platform such as GitHub.com or GitLab.com but, depending on the technology, other potential publishing channels exist (for example, NPM, Maven central, PyPI)
* Does it make sense to publish binaries? If yes, where?
* Define your Web site and communication: What can you do to make your project known? Does it make sense to create a Web site for the project? Are there working groups?
* Plan your project life cycle

### Active or Development Phase

Once the project has got an approval for open sourcing and the code is available and published, the project has entered the active development phase. In this phase, the open source project typically has the following characteristics:

* The source code is publicly visible
* The project community is actively managed
* The project can receive contributions from the community
* Further development is ongoing, based on incoming requirements
* A dedicated team is working on the project and provides support
* Potentially, to make the project better known and to attract more users and contributors, the project is being promoted in talks at open source events, conferences, and so on.

During the active phase, the following aspects should be considered:

* Do marketing: Make the project better known (for example, through blog posts, reaching out to potentially interesting parties/companies, talks at conferences)
* Invest in building and managing the community
* Care for full transparency, every decision shall be made in the public, even if there is no external community yet. This is very important because interested organizations are able to follow all decisions and to build up trust in the project
* Carry out a health check of the project and its community (that is, perform a review of the defined KPI’s and goals)
* Check 3rd party contributions
* Plan further developments
* Support by fixing bugs and security issues

### Mature or Maintenance Phase

At a certain point in time, an open source project becomes mature. This can also be referred to as the "maintenance phase", meaning that only error corrections are made and normally no new functionality is developed. The following aspects characterize this phase:

* The project is being used actively, but from a functional perspective it can be considered as complete or at least no major functional enhancements are necessary
* Contributions mainly focus on bug fixes. Functional enhancements are only minor and are done rarely
* A dedicated team still provides support for the project, but with relatively low efforts
* The team still has to take care of the community, but normally less effort is required compared to projects that are in active development.
* It is good practice to clearly communicate that the project is in the maintenance phase and no or only limited further development can be expected
* The team should perform regular health checks of the open source project and the external community
* Bug fixes and security fixes are still required

### Obsolete or End of Life Phase

An open source project in this phase is characterized by the following properties:

* There is no or only very minor interest in the project
* No further contributions take place
* There are no further developments and no incoming requirements
* No further support takes place
* Possibly, there is no project team available anymore.

During this phase, it is important to consider the legal implications and come up with the appropriate documentation and communication with the community. Since the project has been published, it might be in use. Therefore, the community needs to be informed that the project is no longer maintained. Furthermore, once in this phase the decision must be made whether to archive the project or remove it completely.

## Legal and governance considerations

### Which license to select

Choosing the license for a new open source project is an important decision. Without a license the code can't be used by anybody, even if the code is publically available, for example in a GitHub repository. Choosing a license which is not approved by the OSI as an open source license also effectively makes the code proprietary. This will make it harder to get adoption, especially in most corporate setups, where processes are usually build around the well-known standard open source licenses.

Open source licenses vary in the rights and the obligations they give to users. All open source licenses approved by OSI give users the right to use the software without restriction to specific users or use cases. When distributing open source software, and especially when distributing it with modifications, the obligation vary. The spectrum goes from the so-called copyleft licenses such as the GPL, which require to pass on rights given by the license to users, to permissive licenses, such as the Apache or the MIT license, which allow incorporation in proprietary systems.

When choosing a license the following questions have to be considered:

* **What's the goal of the open source project?** When broad adoption is a priority, a permissive license might be a good choice, when the focus is on building a contributor community, more reciprocal licenses, might have advantages.
* **Is there a license suggested or required by the ecosystem where the project is positioned?** If it's meant to become part of a foundation or an umbrella project then there might be a strong preference for a license, e.g. the Apache license for Apache projects, or the GPL for Linux kernel drivers.
* **How does the license interact with your business model?** When the software you are going to open source is supporting other parts of your business, a permissive license might accelerate adoption. If you are also selling proprietary version of your software, a copyleft license might be a stronger differentiator.
* **Are there depencies or other incorporated code which limit the choice of licenses?** For example when incorporating GPL code, the resulting project has to be GPL as well.

Answering these questions can be challenging and opinions will vary. A simple starting point can be the [choosealicense.com](https://choosealicense.com/). There is a lot of comprehensive material available from various sources, e.g. [Open source licenses: What, which, and why](https://arstechnica.com/gadgets/2020/02/how-to-choose-an-open-source-license/).

It's advisable to set up policies for license selection, so that the decision process is simplified when starting new projects.

### Contributor License Agreement (CLA), Developer Certificate of Origin (DCO)

When running an open source project you need to decide how you are going to check code provenance and if you need additional rights from contributors which are not given by the license. There are mainly three ways how to handle that:

* **"Inbound=Outbound"** - Contributions are accepted under the same license as the project distributes its code. There is no additional paperwork. This is a symmetric setup, where contributors, maintainers, and users have the same rights under the chosen license. It has the lowest barrier for contributors. Some things such as changing the license of the projects become difficult, because that needs approval by every contributor.

* **Developer Certificate of Origin (DCO)** - The [DCO](https://developercertificate.org/) was introduced in Linux kernel development and has been adopted by quite some other projects. It's a statement developers give with each commit by including a "Signed-Off-By" statement in the commit message. With this statement developers explictly declare that they have the rights they need to do the contribution and that they agree that the project is using it. This is still a low barrier, but it gives projects more confidence that code was rightfully contributed. It does not help in cases where the license of the code needs to be changed.

* **Contributor License Agreement (CLA)** - A CLA is an additional agreement between the contributor and the project which gives the project additional rights on top of the rights given by the license. If people contribute on behalf of a company, where the company holds the rights on the work of the contributor, the company has to sign the CLA. There is a variety of different CLAs in use, some mostly confirm the rights already given by the license, some give additional rights such as being able to release the code under a different license, for example when the code is also released under a proprietary license as part of a commercial offering. With a CLA rights are collected at a central place, so changing the license, or rereleasing the code as part of a product with a different license is possible. The assymetry of the agreement, which gives the project more rights than its contributors can impose a bigger barrier for contributions. Requiring a corporate CLA can also be an insurmountable barrier, especially for large corporations, because the effort and legal implications of checking and signing a CLA might outweigh the benefits of contributing. 

You should have a policy for which of these way you use when. "Inbound=Outbound" is a pragmatic way which can work for most projects. The DCO is a good way to make the contribution process more explicit, especially for larger projects with diverse contributors. The CLA makes contributions more difficult and requires additional administrational work and tooling. To get an impression about the additional effort and difficulties especially large corporations face you can check [contributions-to-existing-projects](./02-contributions-to-existing-projects.md#process-for-expressing-company-approval-for-contributions)

### Project governance

An important factor for the success of an open source project is its governance. That comprises the rules, policies, conventions, and culture of the collaboration. It determines factors such as how decisions are taken, who is in control, or who can join a project.

In existing projects governance often has emerged over time, has gone from informal procedures driven by the practices of the project founders to more formally defined governance documented in contribution guides or ultimately instituted through a foundation as formal organization hosting the project.

When starting a new open source project you have to decide about how its governance will look like. This goes beyond deciding on a license. You will also have to decide about ownership of assets such as trademarks or domains and the rules how they can be used. And you will have to decide about policies of how people can become committers or maintainers, how releases and roadmaps are made, or how transparent the decision making process is.

For a project which is meant to attract a broad set of contributors it is important to set up governance which provides a neutral ground, is open to participation by diverse participancts, and is transparent about its decision making. This can be called [open governance](https://opengovernance.dev/). One way to achieve this is to join one of the existing open source foundations. Prominent examples for this are [Kubernetes](https://kubernetes.io/) which is hosted by the [CNCF](https://www.cncf.io/) or the [Eclipse IDE](https://www.eclipse.org/ide/) which is part of the [Eclipse Foundation](https://www.eclipse.org/org/foundation/).

In other cases a company might want to retain more control about the project. This will limit contributions from others but give more freedom in how to steer a project. It requires that there are enough resources allocated to maintain the project. It still is helpful to implement elements of open governance, such as transparency about planning or a permissive trademark policy to increase adoption of the project. Examples for this would be [TensorFlow](https://www.tensorflow.org/) which is run by Google or [Visual Studio Code](https://code.visualstudio.com/) which is run by Microsoft.

For smaller projects, for example technical tools which emerge from work on other projects, a simple and less formal approach to governance can also work. Here the goal is not primarily broad adoption or building a large community, but transparency and ad-hoc collaboration with interested individiuals. Often this kind of project is more driven by technical needs and motivation of developers than by overaching business needs. If such a project is growing its governance can be evolved. This can for example result in a project being transferred to a foundation. Countless examples can be found on [GitHub](https://github.com/explore).

More detailed information and possible starting points for open source governance can be found in the [Minimum Viable Governance](https://github.com/github/MVG) framework or [A Legal Issues Primer for Open Source and Free Software Projects](https://softwarefreedom.org/resources/2008/foss-primer.html).

### Different Project Levels

It can make sense to have different levels for new open source projects ("sandbox", "incubator", "graduated" - these are the different [project levels of CNCF](https://www.cncf.io/projects/), for example). That's a way to classify you open source projects wrt. adoption, maturity and quality criteria that they have to fulfill. The basic idea is that new projects start in a dedicated space (CNCF calls that "sandbox" - at Meta, that's the ["Incubator"](https://github.com/facebookincubator)). In this space, projects can evolve, and check if they reach the goals that have been defined in terms of adoption and quality. If they do, they can be promoted to the next level. If they don't it might be decided to sunset them.

## Community management

For the majority of open source projects, starting a community around that project and receiving contributions is an important if not the primary goal (however, there are also projects where the primary goal for open sourcing is not the creation of a vivid community  - for example building trust by making the source code visible, in this case receiving contributions might have a lower priority). Such a community does not take off by itself. Starting it and keeping it alive requires planning as well as budget and resources. Initial and ongoing activities comprise:

* Promote the project

  This includes presenting at conferences, hosting or sponsor key events, and building new initiatives and programs in your community

* Create a welcoming environment

  This includes creating open-source project policies, guidelines (Basic instructions for maintainers, installation process, instructions for end users) or improve main project communication channels (forums, chat discussions, etc)

* Facilitate collaboration

  Building mentoring programs, adding project documentation (such as how to contribute, How to write and run tests, how the governing board is elected, etc )

It's advisable to assign a community manager to the project who takes care of these tasks. The TODO Group Guide [Starting an open source project](https://todogroup.org/guides/starting/) contains more information in its chapter "Build the community". For further reading, we recommend the TODO Group Guides [Building an inclusive open source community](https://todogroup.org/guides/diversity-inclusion/) and [Building leadership in an open source community](https://todogroup.org/guides/building-leadership/).

### Code of conduct

Creating a welcoming environment where people are safe from harmful behavior by others is an important part of maintaining a healthy community. It's especially important to support a diverse community, where there is no discrimination of under-represented groups, and explicit or implicit bias gets addressed.

A common element in maintaining a healthy community environment is a code of conduct which makes rules for accepted and unaccepted behavior explicit and defines how unacceptable behavior is dealt with. There are examples and templates which can be used as a base for your code of conduct. One popular reusable code of conduct is the [Contributor Covenant](https://www.contributor-covenant.org/) which is used by projects such as Kubernetes, git, Node.js, and many more.

As a company you need to provide a contact email which can be used to report code of conduct violations. You need to make sure that this address is monitored by people who can react in a timely manner and have the competence and ability to initiate adequate actions to address these issues.

## Build an open source metrics strategy when releasing to open source projects

### Goal-question-metric approach

## Technical considerations, tooling and best practices

Appropriate tooling can safe a lot of time and help to automate processes significantly. [Curated list of awesome tools to managee open source](https://github.com/todogroup/awesome-ospo) contains a comprehensive list of proven and recommendable tools.

### User management

Normally, Git providers (GitHub, GitLab, Bitbucket etc.) offer means to define teams of individual users and to define (access) rights on team and on individual level. To be able to use the service of a Git provider, engineers have to create a corresponding account. This account has nothing to do with the company-internal account of an engineer. This imposes some challenges since the access rights of an engineer for an external repository might depend on his/her role in the company or whether he/she is still working for the company (let's assume that an engineer got comprehensive rights for external repositories when he/she was working for your company and that he/she now left the company - you might want to adjust the access rights). But how to do that since the external account of an engineer at a Git provider is independent from his company-internal user account? Somehow a mapping between both accounts is needed. For GitHub there's the open source tool [opensource-portal](https://github.com/microsoft/opensource-portal) available that can help to create such a mapping. It can also be used to implement a self service for joining of GitHub organizations. As part of the process, the tool creates the mapping between the GitHub.com account and the corresponding company-internal user account. The mapping is stored in a database. Based on this, it's easy to create some tooling that regularly checks if all users that are contained in that database are still employed by your company and trigger some activity if that's not the case.

### Setting up a repository

It is good practice that a repository contains a certain set of files (the *health files*). These files contain the basic information about the repository such as description, code of conduct, license, contribution guidelines etc. These files are often provided in [markdown format](https://en.wikipedia.org/wiki/Markdown), but could - depending on the Git provider - be provided in different formats such as [Asciidoc](https://en.wikipedia.org/wiki/AsciiDoc). Here, we assume the default format (which is markdown) and thus use the file suffix *md*.

* *README.md*

  This file is displayed as the *homepage* of the repository. It typically contains information such as repository description, dependencies as well as download, installation and configuration instructions.

* *LICENSE* or *LICENSE.txt*

  Contains the license text for the repository

* *CONTRIBUTING.md*

  Contains information and instruction about how contributions can be made.

* *CODE-OF-CONDUCT.md*

  Contains the code of conduct for the repository.

* *GOVERNANCE.md*

  Contains information about project governance.

* *SECURITY.md*

  Contains instructions about how to report security vulnerabilities for the repository.

* *SUPPORT.md*

  Contains information about how to receive support in case of problems.

The *README.md* and the license text file should be there for all repositories. The other files can be considered as optional and only be created if they are required (if, for example, no contributions are accepted, this information could be put into the *README.md* and a *CONTRIBUTING.md* is not necessary).

To make sure that a certain set of health files is always created, there are different possibilities:

* One possibility is to use template repositories. These are repositories that contain the required set of initial health files. A new repositories can be created/copied from this template repository and thus it contains already the required set of health files. Some Git provider (GitHub, for example) provide [specific means](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file) to create the required health files per default.

* Another possibility is to create repositories with a tool. Such tools create repositories based on some input data via the API's of the Git provider (GitHub.com, GitLab.com, Bitbucket.org etc.). Thus, they can help that repositories are compliant to the company guidelines (contain the required health files **and** team structure, for example). Based on such tools self services for repository creation could be offered that allow development teams creating repositories themselves. Often, companies develop such tools for their specific needs. We (the authors of this document) do not know generic repository creation tools.

### Providing license and copyright information

License and copyright information must be declared properly for an open source project. This is important for consumers of the project as well as for contributors. Furthermore source code often gets copied from one project to another, this makes it mandatory that all files carry license and copyright information (Note that a statement like *For license conditions please check LICENSE.txt* is not suited)

* for the parts of the project that you / your company developed
* but also for external components (i.e. code developed by external parties) that are part of your repositories

The [REUSE tool](https://reuse.software/) from the [Free Software Foundation Europe](https://fsfe.org/) supports the proper declaration of license and copyright information for your project:

* It provides a machine-readable file format for license and copyright information and thus makes it easy for others (scanning tools, for example) to consume that information
* It provides tooling to:
  * add license and copyright information to source code files
  * download and store license texts
  * to lint your repositories to make sure that license and copyright information is available for all files

### CLA/DCO Management

If contributors must accept an CLA or DCO before they can submit their contributions, it's benefitial to automate that process as much as possible. The [TODO Group](https://todogroup.org/) provides a [list of tools](https://github.com/todogroup/awesome-ospo#contributor-license-agreements--developer-certificate-of-originis) that support the management and the sign-off of DCOs or CLA documents. As an example, we describe the [CLA Assistant](https://github.com/cla-assistant/cla-assistant) in more detail.

The CLA Assistant implements a workflow that asks contributors to accept / sign-off a document when a contributor submit the first pull request to a certain repository on GitHub.com. Despite the name of the tool ("CLA Assistant"), it can be used for any type of document that companies require contributors to accept before a pull request can be submitted, including CLA's and DCO's. The document text must be provided as gist on GitHub.com. Which document/gist to be used can be configured on organization and on repository level. The CLA Assistant uses a default logic: If for a certain repository no specific document is configured, the document that is configured on organization level is used. When a contributor submits a pull request for a repository for the first time, the CLA Assistant displays the document text and the contributor can only submit the request if he/she accepts the document. The next time, the same contributor submits a pull request, he/she can do so without having to accept the document again. The information that the contributor accepted the document for that repository is stored in the database of the CLA Assistant and can be retrieved later on. The CLA Assistant is available as hosted offering on https://cla-assistant.io/ or can be self-hosted.

### Credential scanning

Even if open source policies and guidelines explicitely require that credentials such as password, access tokens or other secrets have to be removed from code before it's published, it happens from time to time that unintentionally such important and sensitive data is pushed to public repositories. To detect such situations as quickly as possible (and thus to be able to revoke the published secret and remove that data from public repositories), it's advisable to reguarly execute credential scans for such repositories. Luckily, all well-known code hosting platforms (GitHub.com, GitLab.com etc.) provide such scanning services as part of their offering. We strongly recommend to use that services.

### Quality criteria / CII Best Practices Badge Program

The [Core Infrastructure Initiative](https://www.coreinfrastructure.org/) (CII) created the [CII Best Practices Badge Program](https://bestpractices.coreinfrastructure.org/en). As part of the program, best practices for open source software is defined and a badge system is implemented. Via a [web app](https://bestpractices.coreinfrastructure.org/en/projects), projects can self-certify that they meet the criteria and show a corresponding badge on their website. As of today (May 2022), more than 4724 projects did the assessment.

The CII system consists of three levels (*Passing*, *Silver* and *Gold*). They are building on each other (i.e. the *Silver* level contains all criteria of the *Passing* level plus additional ones). The criteria are structured in clusters such as *Basics*, *Change Control*, *Reporting*, *Quality*, *Security* and *Analytics*.

The CII Best Practices Badge community is [open for contributions](https://github.com/coreinfrastructure/best-practices-badge/blob/12e4f19b713dbbd4170834dabb3b08a816565bd2/CONTRIBUTING.md) (additional criteria, for example).

Overall, the CII Best Practices Badge Program is a good means to verify own projects against commonly accepted best practices. Via the badge projects can document that they meet this criteria.

### Repository Linting

Repository linters are tools that check in an automated way if repositories adhere to the guidelines that a company has defined for its public open source repositories. The [TODO Group](https://todogroup.org/) provides a [list of tools](https://github.com/todogroup/awesome-ospo#project-quality) that can be used for this purpose. Typically, repository linters check criteria such as:

* Do the required files exist in the repository (license file README.md, CONTRIBUTING.md, for example)?
* Do these files contain the required sections?
* Does the repository have a license that is compliant to the company guidelines?
* Does the repository contain the required badges (the REUSE badge or the CII badge, for example)?
* Repository team structure (a certain team structure might be required - at least two administrators, for example)
* Configuration of the repository (are vulnerability alerts activated?, for example)

However, which crteria they check is company-specific and thus, they normally provide the possibility to configure rules (as JSON file, for example, as the [repolinter of the TODO Group](https://github.com/todogroup/repolinter) does). To retrieve the necessary data to execute these checks, the APIs of the Git provider (GitHub.com, GitLab.com, Bitbucket.org etc.) is used. The result of the check is typically provided in a UI. Another option is to automatically create issues in the corresponding repository if checks fail. Typical usage scenarios for such a linter include:

* Check for guideline compliance before a repository is published
* Regular checks after publication

## Build an open source metrics strategy when releasing to open source projects

Once you've established the goals, procedures, and tools for your company's outbound open source plan, it's always useful to monitor and track the overall health of open source projects the company engages with as they grow and mature.

Before thinking about which tool should be used to track project health, a good alternative on how to do this is to establish a full metrics strategy following the goal-question-metrics approach. This approach is used in communities focused on community health analytics metrics standards and software, such as [CHAOSS](https://chaoss.community), one of the projects under the Linux Foundation umbrella.

**Defining community health goals**

Sometimes is better to start small and define 2 or 3 main goals first before getting overwhelmed by metrics. If you don't know where to start, CHAOSS offers a set of metrics based on different focus-areas and goals when measuring project health that can help you get started in measuring the health of the open-source projects that matter to your organization:

* Common Metrics
* Diversity and Inclusion
* Evolution
* Risk
* Value
* App Ecosystem

**Creating questions and building metrics around**

Metrics should be answering specific questions that are aligned with the previous goals established.

For instance, if one of your company's goals is to understand the community footprint within a project, one good question can be "What’s the presence and influence of organizations within the open source ecosystem?". In order to solve this, one useful metric can be the Elephant Factor (the minimum number of organizations whose employees perform 50% of the total contributions).

There are great tooling to help you measure different community health analytics metrics, for instance, GrimoireLab, LFX, or Augur.

For further information about Tools for tracking project health, check this dedicated section from one of the [TODO Guides](https://todogroup.org/guides/management-tools/#tools-for-tracking-project-health)
