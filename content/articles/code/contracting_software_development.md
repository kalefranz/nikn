date: 2013-05-13
category: code
tags: software management, contracting
title: On Contracting Software Development
local_id:

**Core Assertion:** The company owns the code, not the contractor.

If you're a contractor, why wouldn't you want to keep the actual source to
yourself?  You lock the company your contacting for into using your services in
perpetuity.  Good for the contractor; *very* bad for the procuring company.  My
guess is that less-than-competent and more "old school" contractors who aren't
able to keep up with technology's pace will push this tactic for their own job
security. But the contractor lock-in prevents the company from moving forward
with their product using another contractor if the relationship sours with the
current contractor.  It also prevents the company from transitioning away from
contract work to an in-house development team.

The rest of this document contains steps necessary to have the best chance for
getting quality code from a contractor.  I would consider each item mandatory.
There are also plenty of "nice to haves," but I want to keep this right now to
what I consider mandatory.

### You control the source control ###

Your contractor will use the source control system that you provide.  It is your
company's own source control system, and you give and revoke permissions to your
own repositories.  Use Git.  Everybody uses Git today.  If your contractor
complains that Git is "too hard," run away as fast as you can.  Create an account
on either [github.com](http://www.github.com) or
[bitbucket.com](http://www.bitbucket.com).  Both are widely used and great
products.

### Demand documentation ###

Documentation of the system that your contractor is designing should be part of
the deal.  Documented topics would include, for example,

* thorough explanation of the system architecture
* thorough documentation of any API layers
* code deployment [run book](http://en.wikipedia.org/wiki/Runbook)

Like source code revision control, *you* should own the documentation and it
should be kept in a location that *you* control.  My recommendation is
Atlassian's [Confluence](http://www.atlassian.com/software/confluence/overview/team-collaboration-software)
product.

One critical part of quality software is readable and comprehensible source code.
Professional programmers in a team environment should be adept at writing in-code
comments where necessary and in general write code that is overall
self-documenting.  *Not all code is self documenting!  Writing self-documenting
code takes deliberate effort.  Just because code compiles, it is not therefore
"self-documenting"!!*  Advice here would be to  require that every public
function (within reason, so exclude getters, setters, etc.) have a
language-relevant documentation block (docstring, javadoc, etc).

### Source code tests ###

Professional programmers write unit tests.  To be sure that the code being
developed runs as it should, demand unit tests be written by the programmers as
part of the project.  [Code coverage](http://en.wikipedia.org/wiki/Code_coverage)
is a metric that describes what percent of your source code is "touched" or
covered by unit tests.  Include a code coverage stipulation as part of your
contract; a reasonable number is somewhere in the neighborhood of 80%.  Note
that there is a danger with using code coverage as a sole metric for test
quality.  From [this](http://stackoverflow.com/a/695888/2127762) StackOverflow post:

> Code coverage tells you what you definitely **haven't** tested, not what you **have**.

Just realize that there are pitfalls to the code coverage metric and be aware of them.

### Continuous Integration ###

There should be a
[continuous integration](http://martinfowler.com/articles/continuousIntegration.html)
environment set up for the code base.  Whether you set this up or the contractor
really doesn't matter, as long as you definitely have access to monitor it.  The
value to you as the company will be in the ability to monitor project progress,
monitor code coverage and other code quality metrics, and monitor the status of
the current build (code compiling and all tests passing).
[Jenkins](http://jenkins-ci.org) is certainly the most main-stream CI
technology, and you can apparently get a hosted version
[here](http://www.cloudbees.com/jenkins-enterprise-by-cloudbees-overview.cb).
Jenkins itself is free and open source, so you can deploy it to your own local
or cloud servers too.  Another interesting option might be
[Travis CI](http://travis-ci.com).

### DevOps considerations ###

DevOps tasks are all those that deal with keeping your software running
*in production*. Are your servers healthy, or are they becoming overburdened?
Is your application even running, or has something crashed?  Your architecture
might be one that has several interdependent components, and that the front door
is working properly doesn't necessarily mean a portion of the system hasn't
crashed elsewhere.  Server and application health requires constant, automated
monitoring.

The area of DevOps is often separate from the software development itself.  Make
sure you have a DevOps strategy for system monitoring, and have the appropriate
knowledge or resources to take action when something fails.
