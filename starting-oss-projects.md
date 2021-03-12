# Starting open source projects

## Motivation

## Preparation

## Which license to select

## Budget

## ...	

## Legal aspects

## CLA’s, DCO’s 

## Project governance

### Code of conduct

### Templates (issues, PR’s)

### “Health files” (-> GitHub health files)

## Tools

### Credential scanner

### Reuse tool

### CLA Assistant

## Company-based vs. foundation-driven

### When to select which approach

### Leveraging a foundation (such as Eclipse)

## Lifecycle mgmt

The life cycle of an open source project describes the stages in which the project evolves, from its conception to its retirement or end of life stage. Typically, a project originates to solve a specific problem. It may become obsolete either because the problem does not exist anymore or because other projects are better suited to solve the problem. The figure below shows the different stages an open source project may undergo.

![Typical lifecycle of an open source project](./img/OSS-lifecycle.png)

### Planning or Concept Phase

This is the starting point of every open source project. It can also be referred to as the “initiation phase”. Normally, at this stage, only an idea exists or a specific problem has been identified which requires solution. In this phase, the open source project typically has the following characteristics:

* The problem that the project intends to solve has been clearly defined
* There is either no source code available yet or the source code is only internally available. In the first case, the project only exists as idea; in the second case, the project may have been started as an company-internal project and has not been published yet
* Possibly, the idea has been already shared with the community to get feedback. However, note that this sharing such ideas that so far have only been discussed company-internally requires approval in advance.

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
* Does it make sense to donate the code to a vendor-neutral, non-profit organization (that is, an open source foundation), or retain some control by owning and running the project under the responsibility of your company? Note that this decision depends on the project and may also be taken later in the life cycle. Typically, a project first needs to be published and generate interest in the community before it is handed over to a third-party organization.
* Launch check list. For example, see the [checklist of the Linux Foundation](https://www.linuxfoundation.org/en/resources/open-source-guides/starting-an-open-source-project/#checklist)
* Set up an open source project governance. It establishes how to contribute to or maintain a project.
* Determine the tools and infrastructure the project members will use
* Carry out a technical review

  * Ensure that all critical content is removed from the project before publishing it. For example:

    * Dependencies to non-public components
    * Internal comments, references to other internal code, and the like
    * Access tokens and the like

  * Ensure coding style is consistent

* Where will the code be published? Typically, it will be in a company-owned organization on a code hosting platform auch as Githuib.com or GitLab.com but, depending on the technology, other potential publishing channels exist (for example, NPM, Maven central, PyPI)
* Does it make sense to publish binaries? If yes, where?
* Define your Web site and communication: What can you do to make your project known? Does it make sense to create a Web site for the project? Are there working groups?
* Plan your project life cycle

#### Different Project Levels

It can make sense to have different levels for new open source projects ("sandbox", "incubator", "graduated" - these are the different [project levels of CNCF](https://www.cncf.io/projects/), for example). That's a way to classify you open source projects wrt. adoption, maturity and quality criteria that they have to fulfill. The basic idea is that new projects start in a dedicated space (CNCF calls that "sandbox" - at Facebook, that's the ["Incubator"](https://github.com/facebookincubator)). In this space, projects can evolve, and check if they reach the goals that have been defined in terms of adoption and quality. If they do, they can be promoted to the next level. If they don't it might be decided to sunset them.

### Active or Development Phase

Once the the project has got an approval for open sourcing and the code is available and published, the project has entered the active development phase. In this phase, the open source project typically has the following characteristics:

* The source code is publicly visible
* The project community is actively managed
* The project can receive contributions from the community
* Further development is ongoing, based on incoming requirements
* A dedicated team is working on the project and provides support
* Potentially, to make the project better known and to attract more users and contributors, the project is being promoted in talks at open source events, conferences, and so on.

During the active phase, the following aspects should be considered:

* Do marketing: Make the project better known (for example, through blog posts, reaching out to potentially interesting parties/companies, talks at conferences)
* Invest in building and managing the community
* Carry out a health check of the project and its community (that is, perform a review of the defined KPI’s and goals)
* Check 3rd party contributions
* Plan further developments
* Support by fixing bugs and security issues

### Mature or Maintenance Phase

At a certain point in time, an open source project becomes mature. This can also be referred to as the "maintenance phase", meaning that only error corrections are made and normally no new functionality is developed. The following aspects characterize this phase:

* The project is being used actively, but from a functional perspective it can be considered as complete or at least no major functional enhancements are necessary
* Contributions mainly focus on bug fixes. Functional enhancements are only minor and are done only rarely
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

### Quality criteria (CII Badge …)

### Day-2-ops (CI/CD, security, license scanning, …)

### Community mgmt (-> TODO group paper)

### Analytics

#### Tools

### Sunsetting a project (-> TODO group paper)

# Ideas:

## Extract target group-specific 1-pagers

## Developers

## Management

---------------------------------------------------------------------------------------------------------------------------
Launching a new OSS project is comparable to a product introduction and it is, at first hand, a software development project - there is no difference to an internal software development project concerning planning, budget, staffing, testing etc. - the only difference is that everything happens in the public area. Be aware that publicly available source code is the “business card” of the organization to the software  ecosystem, and it is also the “business card” of its maintainers.

When thinking about to start an own OSS project there are several phases you should consider:

![oss-projcet-process](./img/LaunchinOSSProject.PNG)

## Why to start an OSS project
The phase “why to start an OSS project” is very important and one shall have a clear picture about the “why” after this phase, because the answer to the “why” influences heavily subsequent decisions - like the license, whether to choose a CLA or DCO or “license-in =  license-out”, etc. [ToDo] add more

## Plan the OSS project
Prepare for launching the project
* Check source code
* REUSE conformance
* Define project governance:	
* charter
* code of conduct
* contribution guidelines
* CLA/DCO/...
* issue template
* PR template
* versioning
