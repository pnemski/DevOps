from buildbot.plugins import steps

factory.addStep(steps.Git(repourl='github.com/pnemski/DevOps.git', mode='full',
                          method='clobber', submodules=True))
