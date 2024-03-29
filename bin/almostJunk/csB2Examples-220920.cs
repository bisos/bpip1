#!/bin/env python
# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: A =CmndSvc= for running CS examples individually or collectively.
#+end_org """

""" #+begin_org
* [[elisp:(org-cycle)][| /Control Parameters Of This File/ |]] :: dblock controls and classifications
#+BEGIN_SRC emacs-lisp
(setq-local b:dblockControls t) ; (setq-local b:dblockControls nil)
(put 'b:dblockControls 'py3:cs:Classification "cs-mu") ; Main Multi-Unit CommandSvc
#+END_SRC
#+RESULTS:
: cs-mu
#+end_org """

####+BEGIN: b:prog:file/proclamations :outLevel 1
""" #+begin_org
* *[[elisp:(org-cycle)][| Proclamations |]]* :: Libre-Halaal Software --- Part Of Blee ---  Poly-COMEEGA Format.
** This is Libre-Halaal Software. © Libre-Halaal Foundation. Subject to AGPL.
** It is not part of Emacs. It is part of Blee.
** Best read and edited  with Poly-COMEEGA (Polymode Colaborative Org-Mode Enhance Emacs Generalized Authorship)
#+end_org """
####+END:

####+BEGIN: b:prog:file/particulars :authors ("./inserts/authors-mb.org")
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars |]]* :: Authors, version
** This File: NOTYET
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:py3:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['csB2Examples'], }
csInfo['version'] = '202209125126'
csInfo['status']  = 'inUse'
csInfo['panel'] = 'csB2Examples-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/COMEEGA/_nodeBase_/fullUsagePanel-en.org][BISOS COMEEGA Panel]]
Module description comes here.
** Relevant Panels:
** Status: In use with blee3
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
*** TODO complete fileName in particulars.
#+end_org """

####+BEGIN: b:prog:file/orgTopControls :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Controls |]] :: [[elisp:(delete-other-windows)][(1)]] | [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
#+end_org """
####+END:

####+BEGIN: b:py3:file/workbench :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Workbench |]] :: [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: bx:cs:python:icmItem :itemType "=PyImports= " :itemTitle "*Py Library IMPORTS*"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =PyImports=  [[elisp:(outline-show-subtree+toggle)][||]] *Py Library IMPORTS*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:framework/imports :basedOn "classification"
""" #+begin_org
** Imports Based On Classification
#+end_org """
from bisos import b
from bisos.b import cs
from bisos.b import b_io

import collections
####+END:

""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] /csuList emacs-list Specifications/  [[elisp:(blee:org:code-block/above-run)][ ~Eval Below~ ]] [[elisp:(org-cycle)][| ]]
#+BEGIN_SRC emacs-lisp
(setq  b:py:cs:csuList
  (list
   "bisos.b.cs.ro"
   "blee.icmPlayer.bleep"
   "bisos.examples.pattern_csu"
   "bisos.examples.pyRunAs_csu"
   "bisos.examples.io_csu"
   "bisos.examples.parsArgsStdinCmndResult_csu"
   "bisos.examples.subProcOps_csu"
   "bisos.examples.platformConfigs_csu"
   "bisos.b.fpCls"
   "bisos.b.clsMethod_csu"
   "bisos.examples.fp_csu"
   "bisos.examples.roPy_csu"
 ))
#+END_SRC
#+RESULTS:
| bisos.b.cs.ro | blee.icmPlayer.bleep | bisos.examples.pattern_csu | bisos.examples.pyRunAs_csu | bisos.examples.io_csu | bisos.examples.parsArgsStdinCmndResult_csu | bisos.examples.subProcOps_csu | bisos.examples.platformConfigs_csu | bisos.b.fpCls | bisos.b.clsMethod_csu | bisos.examples.fp_csu | bisos.examples.roPy_csu |
#+end_org """

####+BEGIN: b:py3:cs:framework/csuListProc :pyImports t :csuImports t :csuParams t
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] ~Process CSU List~ with 12 in csuList pyImports=t csuImports=t csuParams=t
#+end_org """

from bisos.b.cs import ro
from blee.icmPlayer import bleep
from bisos.examples import pattern_csu
from bisos.examples import pyRunAs_csu
from bisos.examples import io_csu
from bisos.examples import parsArgsStdinCmndResult_csu
from bisos.examples import subProcOps_csu
from bisos.examples import platformConfigs_csu
from bisos.b import fpCls
from bisos.b import clsMethod_csu
from bisos.examples import fp_csu
from bisos.examples import roPy_csu


csuList = [ 'bisos.b.cs.ro', 'blee.icmPlayer.bleep', 'bisos.examples.pattern_csu', 'bisos.examples.pyRunAs_csu', 'bisos.examples.io_csu', 'bisos.examples.parsArgsStdinCmndResult_csu', 'bisos.examples.subProcOps_csu', 'bisos.examples.platformConfigs_csu', 'bisos.b.fpCls', 'bisos.b.clsMethod_csu', 'bisos.examples.fp_csu', 'bisos.examples.roPy_csu', ]

g_importedCmndsModules = cs.csuList_importedModules(csuList)

def g_extraParams():
    csParams = cs.param.CmndParamDict()
    cs.csuList_commonParamsSpecify(csuList, csParams)
    cs.argsparseBasedOnCsParams(csParams)

####+END:


ExampleFilePars = fp_csu.ExampleFilePars  # exec/eval-ed as __main__.ClassName


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "CmndSvcs" :anchor ""  :extraInfo "Command Services Section"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _CmndSvcs_: |]]  Command Services Section  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: bx:cs:py3:section :title "CS-Examples"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *CS-Examples*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "examples" :extent "verify" :ro "noCli" :comment "FrameWrk: ICM Examples" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<examples>> =FrameWrk: ICM Examples=parsMand= parsOpt= argsMin=0 argsMax=0 ro=noCli pyInv=
#+end_org """
class examples(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}
    rtInvConstraints = cs.rtInvoker.RtInvoker.new_noRo() # NO RO From CLI

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:
        """FrameWrk: ICM Examples"""
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:
        def cpsInit(): return collections.OrderedDict()
        def menuItem(verbosity): cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
        #def execLineEx(cmndStr): cs.examples.execInsert(execLine=cmndStr)

        #logControler = b_io.log.Control()
        #logControler.loggerSetLevel(20)

        cs.examples.myName(cs.G.icmMyName(), cs.G.icmMyFullName())

        cs.examples.commonBrief()

        bleep.examples_icmBasic()

        cs.examples.menuChapter('=Misc=  *Facilities*')

        cmndName = "dirCreateExamples" ; cmndArgs = "" ;
        cps=cpsInit() ;
        menuItem(verbosity='little')

        cmndName = "exceptionExamples" ; menuItem(verbosity='little')

        cmndName = "subProcOpsExamples" ; menuItem(verbosity='little')

        pattern_csu.examples_csu(sectionTitle="default")

        pyRunAs_csu.examples_csu(sectionTitle="default")

        io_csu.examples_csu(sectionTitle="default")

        parsArgsStdinCmndResult_csu.examples_csu(sectionTitle="default")

        subProcOps_csu.examples_csu(sectionTitle="default")

        platformConfigs_csu.examples_csu(sectionTitle="default")

        fp_csu.examples_csu(sectionTitle="default")

        roPy_csu.examples_csu(sectionTitle="default")

        cs.examples.menuChapter('=Tests=  *All Examples As Tests*')
        cmndName = "allExamplesAsTests" ; menuItem(verbosity='none')

        return(cmndOutcome)

####+BEGIN: bx:cs:py3:section :title "CS-Commands"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *CS-Commands*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "dirCreateExamples" :extent "verify" :comment "" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<dirCreateExamples>>parsMand= parsOpt= argsMin=0 argsMax=0 pyInv=
#+end_org """
class dirCreateExamples(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:
        docStr = """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Various examples for creation of directories.
- examples and smoke unit test for file: ../bisos/bpf/dir.py
        """
        if self.docStrClassSet(docStr,): return cmndOutcome

        b.dir.createIfNotThere("/tmp/t1")

        return cmndOutcome



####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "exceptionExamples" :extent "verify" :comment "" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<exceptionExamples>>parsMand= parsOpt= argsMin=0 argsMax=0 pyInv=
#+end_org """
class exceptionExamples(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:

        b.exception.terminate("PREV-Term", "NEXT-Term", "Some Termination Message")

        # terminate, terminates. So, below is unreachable.
        #

        try:
            raise b.exception.TransitionError("PREV", "NEXT", "Some Message")
        except b.exception.TransitionError as inst:
            print(inst)

        return cmndOutcome



####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "allExamplesAsTests" :extent "verify" :comment "" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<allExamplesAsTests>>parsMand= parsOpt= argsMin=0 argsMax=0 pyInv=
#+end_org """
class allExamplesAsTests(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org \
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] This is an example of a CmndSvc with lots of features.
        #+end_org """)

        myName = cs.G.icmMyName()

        verbosity = " -v 20 "

        print(self)

        opOutcome = b.subProc.WOpW(invedBy=self.cmndOutcome, log=1).bash(
                f"""{myName}  {verbosity} -i sameInstanceEx""",
        )

        print(opOutcome)

        #return opOutcome

        if b.subProc.WOpW(invedBy=self, log=1).bash(
                f"""{myName}  {verbosity} -i sameInstanceEx""",
        ).isProblematic():  return(b_io.eh.badOutcome(cmndOutcome))

        if b.subProc.WOpW(invedBy=self, log=1).bash(
                f"""{myName}  {verbosity} -i runAsUser""",
        ).isProblematic():  return(b_io.eh.badOutcome(cmndOutcome))

        if b.subProc.WOpW(invedBy=self, log=1).bash(
                f"""{myName}  {verbosity} -i outStreamsExamples""",
        ).isProblematic():  return(b_io.eh.badOutcome(cmndOutcome))

        # if b.subProc.WOpW(invedBy=self, log=1).bash(
        #         f"""{myName}  {verbosity} -i subProcOpsWithArgs echo this and that""",
        # ).isProblematic():  return(io_eh.badOutcome(cmndOutcome))

        if b.subProc.WOpW(invedBy=self, log=1).bash(
                f"""{myName}  {verbosity} --par1Example="par1Mantory" --par2Example="par2Optional" -i parsArgsStdinCmndResult""",
        ).isProblematic():  return(b_io.eh.badOutcome(cmndOutcome))

        if b.subProc.WOpW(invedBy=self, log=1).bash(
                f"""{myName}  {verbosity} -i pyCmndInvOf_parsArgsStdinCmndResult""",
        ).isProblematic():  return(b_io.eh.badOutcome(cmndOutcome))

        return cmndOutcome


####+BEGIN: b:py3:cs:framework/main :csInfo "csInfo" :noCmndEntry "examples" :extraParamsHook "g_extraParams" :importedCmndsModules "g_importedCmndsModules"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] ~g_icmMain~ (csInfo, _examples_, g_extraParams, g_importedCmndsModules)
#+end_org """

if __name__ == '__main__':
    cs.main.g_csMain(
        csInfo=csInfo,
        noCmndEntry=examples,  # specify a Cmnd name
        extraParamsHook=g_extraParams,
        importedCmndsModules=g_importedCmndsModules,
    )

####+END:

####+BEGIN: b:py3:cs:framework/endOfFile :basedOn "classification"
""" #+begin_org
* *[[elisp:(org-cycle)][| ~End-Of-Editable-Text~ |]]* :: emacs and org variables and control parameters
#+end_org """

#+STARTUP: showall

### local variables:
### no-byte-compile: t
### end:
####+END:
