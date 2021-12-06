# How to contribute to OSS projects 

Building better relationships with the open source ecosystem has its own set of challenges, but it becomes easier if you have a clear plan to follow. Here are some guidelines to a number of practices that organizations can adopt. 

## Define your open source goal and strategy

 Your open source strategy connects the plans for managing, participating in, and creating open source software with the business objectives that the plans serve. This can open up many opportunities and catalyze innovation. The TODO GRoup offers a dedicated guide to [Setting an Open Source Strategy](https://todogroup.org/guides/strategy/)

## Establish open source guiding principles and processes

### Guiding principles

The procedure described in the following is designed to ensure that the company interests and its employees are protected. We also need to make sure that contributions are in line with copyright law, export regulations, data protection regulations and open source development best practices. On the other hand, procedural burden for all to be involved stakeholders should be low and the approval procedure should not take too much time.


### General structure and scope of the process

**Lean procedure**

* The tasks to be carried out by the developer shall be clear, simple, and cause as little effort as possible
* The potential complexity of the “backend tasks” should not be visible to the developer
* The current status of the request shall be visible to the developer at any time

**Boundary conditions**

* Protect our employees and our business interests
* Act in compliance with law, internal and external regulations
* Provide transparency to the decision makers on what and how much of the companies code and IP will be affected by the contribution
* All the contributions shall be made with the “company”-email (similar for the github activity) so that all contributions of the company can be identified easily.
* Respect the rules and customs of the OSS ecosystem and of the target OSS project

### Process for expressing company approval for contributions

**Why is it needed?**

Why is there a need for a certain procedure at all? First of all the copyright law requires it.

For example the [German copyright act states in Section 69b](https://www.gesetze-im-internet.de/englisch_urhg/englisch_urhg.html#p0522):

	> Authors in employment or service relationships
    > (1) Where a computer program is created by an employee in the execution of his duties or following the instructions of his employer, the employer exclusively shall be entitled to exercise all economic rights in the computer program, unless otherwise agreed.

This means that all the software developed in this context is the property of the employer i.e. the company the developer is working for. At least the German copyright act does not limit the proprietorship to code developed during working hours or within the company IT infrastructure, it only scopes the context.

Secondly a procedure is required to protect the companies business interests as well as to protect the employee. Last but not least public code is like the business card of a company as well as of the developer who has written the code.

The more complex the business environment in which the code to publish was developed, the more stakeholders need to be involved. The picture below shows a procedure that involves all functions, even in a complex setup.

**Outbound CLA/DCO**

Some OSS projects as well as some OSS Foundations require a Contributor License Agreement (CLA) before they accept contributions. We know at least two different types of CLAs:
* Corporate Contributor License Agreement (CCLA)
* Individual Contributor License Agreement (ICLA)
Whether none, one or both are required for contributions is usually described in files like "Contributing.md" in the project repositories. The [CCLA](https://www.apache.org/licenses/cla-corporate.pdf) and the [ICLA](https://www.apache.org/licenses/icla.pdf) authored by the Apache Foundation are the de facto standard of CLAs and many OSS projects have adopted either one or both of them.

The purpose of a CLA or a Developers Certificate of Origin (DCO) is to provide confidence to the OSS project that the contributor is entitled to submit the contribution. A DCO is a more lightweight approach compared to a CLA.

The price for improved confidence for the OSS project is more overhead in the organization the contributor is working for. Especially in case of large corporations with several affiliates the effort of evaluating, signing and maintaining a CCLA shall not be underestimated.

Why is a CCLA causing additional effort in large organziations, let's briefly look at the CCLA of the Apache Foundation as an example:
* The CCLA is a contract - in many organizations the "four eyes principle" is implemented - a contract has to be signed by two persons, who have the right to sign contracts in the name of the organization - the required involvement of probably two more stakeholders requires additional effort in briefing them
* Usually a CCLA covers not only the specific legal entity the contributor is working for, it also covers all affiliates:
	> For legal entities, the entity making a Contribution and all other entities that control, are controlled by, or are under common control with that entity are considered to be a single Contributor. For the purposes of this definition, "control" means (i) the power, direct or indirect, to cause the direction or management of such entity, whether by contract or otherwise, or (ii) ownership of fifty percent (50%) or more of the outstanding shares, or (iii) beneficial ownership of such entity.
	 
* The CCLA includes besides the copyright grant a patent grant. This is fine, nevertheless inside the organization the "IP department" needs to be involved in the evaluation process of the CCLA and for the specific contribution the "IP department" need to sync with all affiliates
* The CCLA needs to be analysed by the "Legal department" of the organization.

Some CCLA are requiring that the copyright of the contributions are assigned to the OSS project/Foundation. Copyright assignment is a topic which, causes even more effort and might not be accepted at all.

Besides the above mentioned additional effort the CCLA places additional "maintanence effort" to the organization, because it requires that the organziation nominates all entitled contributors by name to the CCLA requiring party.
> It is your responsibility to notify the Foundation when any change is required to the list of designated employees authorized to submit Contributions on behalf of the Corporation, or to the Corporation's Point of Contact with the Foundation.
	
Implementing this requirement is causing quite some organizational effort:
* The signed CCLA has to made available inside the organization - This can be done via publishing the CCLA on the OSPOs website at a location which can be found easily be the employees (e.g. it might be usefull to have a "top level page" named CCLAs, this page then contains a list of "signed CCLAs", a list of "CCLAs under evaluation", a list of "denied CCLAs".)
* All affiliates need to be informed and a procedure needs to be defined how the affiliates can nominate/ de-nominate contributors working for them. This becomes even more challenging in case an affiliate has no access to the intranet of the signing entity. In this case the signed CCLA or the information about the signed CCLA needs to be sent to the OSPOs of all affiliates, in case an affiliate has no OSPO set up, the information has to be routed to the function, which is in charge of sw development. All affiliates need to provide the names of nominated contributors or former contributors, who shall not be entitled anymore to do contributions to the OSPO of the signing entity, which then has to inform the Foundation/project about the change of the list of contributors. 
* Publishing the list of contributors inside the organization and disclosing it to the Foundation/project might also require the approval of the data protection officers of the involved entities

All this additional effort may hold organizations off to contribute small bugfixes or patches or even new features to the upstream OSS projects and puts them to risk of private forks and thus a lot of additional development effort in the long run. Thus the decision not to contribute needs to be taken very carefully. 

A DCO in contrast to a CLA is a much more lightweight procedure. It was introduced to enhance the confidence that contributions to the Linux kernel are made "legally correct" by the contributors. The [DCO version 1.1](https://developercertificate.org/) is used by many OSS projects.

The main difference of a DCO compared to a CLA is, that a DCO is not a contract, it is a kind of attest of the specific contributor that he/she is entitled to submit a concrete contribution. All the effort which has to be spend to get a CLA signed and maintained is not needed. The only tasks which have to be carried out are:
* Evaluation of the DCO by the "Legal department"
* Evaulation by the "IP department"
* Evaluation by the specific contributor, whether it is acceptable for him/her
Since the DCO version 1.1 is the "standard" the "Legal"- and "IP department" only have very little effort to spend.


**Procedure for contributions to existing projects**

An example for a full process for doing contributions looks like this:

![contributions](./img/template-contribs.JPG)

The procedure described above is not suited for frequent contributors and/or contributors who are working “upstream” in their daily work. For these developers different procedures need to be established in order to avoid loading them with “unproductive” work. This is described in the section about contribution models.

## Contribution models

The following approaches are suited for such developers:

* small contributions model
* major to major release model
* full trust model

![small-contributions](./img/small-contributions.JPG)

**Small contributions Model or trivial contributions**

A small or trivial contribution is a rather small and simple change to already existing open source software. Typical cases found in this category are bug fixes and error corrections with no or low Intellectual Property value.
A change is not trivial if:
* Functionality is added or changed.
* The interface of the open source software component is changed.
* It is an optimization that more than insignificantly increases performance.
* It contains a design or an algorithm that wouldn’t be obvious for a software engineer.

This procedure scopes small contributions. It can be followed for small or trivial contributions following the initial contribution to a particular OSS project or component. The initial contribution has to implement the entire procedure described above, because CLAs / DCOs etc. have to be checked  and signed in case the particular project requires them.
After the initial contribution all subsequent small contributions can be contributed directly to the OSS project without the need to follow the defined process no matter which version of the OSS project.

**Major to major release model**

This procedure scopes the release cycle of the OSS project where contributions shall be made to. It has the same “starting point” like any other contribution - the initial contribution has to implement the entire procedure in order to check CLAs / DCOs and to have the documented permission to contribute to a specific project. After the initial contribution all subsequent contributions during the development of a new major release can be contributed to the OSS project without the need to go through the approval process. There is no size limitation for contributions. The contributions can range from a trivial bug fix to adding new features, changing interfaces, refactoring and so on. After the release of a major version of the project a new approval procedure has to be kicked off for the first contribution after the major release.

**Full trust model**

The full trust model can be applied to developers who have already successfully worked under the major to major release model. It is an incentive for the employee and a sign of confidence of the employer towards the employee. Basically it is the allowance for the developer to work “upstream” without any approval procedure. Since this model shall only be applied after the developer worked successfully under the major to major release model, there is no need for an  “initial” contribution with the entire approval procedure, although it makes sense in order to have it documented.

The Major to major release model as well as the full trust model shall only be executed by  senior developers, who are specially trained in copyright principles, have a good understanding of the business interests of the company they are working for, practise “an ownership culture” and have already deep experience in the open source ecosystem.
In order to track all the contributions the developers shall contribute with their official email / github id.

**Clearing projects for contributions**

Another model is to provide approval for specific projects. These projects are checked, e.g. by the OSPO, and if everything is in place to allow contributions, they are cleared for contributions by employees. Then there is no individual approval for each specific contribution required, but only if general conditions of the project change, such as license or introduction of a CLA, etc.

Prerequisite for such a model is that contributors are qualified to do contributions autonomously. This can be achieved by making sure contributors have received training and/or tracking and approving who can contribute to which repository.

**Spare time contributions**

TODO: See [issue #2](https://github.com/Open-Source-Compliance/outbound-oss/issues/2).

**Trainings**

Contributors to open source projects will need to act with a certain degree of autonomy to be effective. For some corporate software developers it will also be new to participate in open source communities. For these reasons it's important to support corporate contributors and provide them with training or similar means to develop the understanding and skills to act as good citizens of the open source world on behalf of your company.

This can be achieved with mentoring, good practice guides, or trainings which cover the following topics:

* Essentials of legal implications of open source, such as copyright, licensing, CLAs, DCOs, trademarks
* Awareness of your corporate rules and policies for contributing to open source
* Open source community culture
* Typical open source development procedures
* Open source governance in its different forms such as foundations or single-vendor projects
* Working in public
* Dealing with conflict of interests between open source project and company
* Where to get internal support in case of doubt or questions
