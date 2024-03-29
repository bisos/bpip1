#!/bin/env python
# -*- coding: utf-8 -*-
"""\
* *[PyICM]* :: SERVICE: create a non-interactive git-shell processing account. USER: issues triggers.
"""

import typing

icmInfo: typing.Dict[str, typing.Any] = { 'moduleDescription': ["""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Description:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Xref]          :: *[Related/Xrefs:]*  <<Xref-Here->>  -- External Documents  [[elisp:(org-cycle)][| ]]

**  [[elisp:(org-cycle)][| ]]   Scope And Purpose                                                  :Overview:
*** +
*** Purpose: Allows for USER to trigger immediate actions on SERVICE using git-shell and git hooks.
*** Scope: This ICM covers both SERVICE and USER sides.
*** -
**      [End-Of-Description]
"""], }

icmInfo['moduleUsage'] = """
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Usage:* | ]]
** +
** On SERVICE, run fullServiceUpdate -- create git-repos and install git-hooks.
** On USER, run fullUserUpdate -- install keys --  clone git-repos and push.
**      [End-Of-Usage]
"""


icmInfo['moduleStatus'] = """
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Status:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Info]          :: *[Current-Info:]* Under Development -- General TODO List [[elisp:(org-cycle)][| ]]
** TODO complete implementation of all commands.
**      [End-Of-Status]
"""

"""
*  [[elisp:(org-cycle)][| *ICM-INFO:* |]] :: Author, Copyleft and Version Information
"""
####+BEGIN: bx:icm:py:name :style "fileName"
icmInfo['moduleName'] = "cntnrGitShTriggers"
####+END:

####+BEGIN: bx:icm:py:version-timestamp :style "date"
icmInfo['version'] = "202112191841"
####+END:

####+BEGIN: bx:icm:py:status :status "Production"
icmInfo['status']  = "Production"
####+END:

icmInfo['credits'] = ""

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/update/sw/icm/py/icmInfo-mbNedaGplByStar.py"
icmInfo['authors'] = "[[http://mohsen.1.banan.byname.net][Mohsen Banan]]"
icmInfo['copyright'] = "Copyright 2017, [[http://www.neda.com][Neda Communications, Inc.]]"
icmInfo['licenses'] = "[[https://www.gnu.org/licenses/agpl-3.0.en.html][Affero GPL]]", "Libre-Halaal Services License", "Neda Commercial License"
icmInfo['maintainers'] = "[[http://mohsen.1.banan.byname.net][Mohsen Banan]]"
icmInfo['contacts'] = "[[http://mohsen.1.banan.byname.net/contact]]"
icmInfo['partOf'] = "[[http://www.by-star.net][Libre-Halaal ByStar Digital Ecosystem]]"
####+END:


####+BEGIN: bx:icm:python:topControls :partof "bystar" :copyleft "halaal+minimal"
"""
*  [[elisp:(org-cycle)][|/Controls/| ]] :: [[elisp:(org-show-subtree)][|=]]  [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(delete-other-windows)][(1)]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
"""
####+END:
####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/software/plusOrg/dblock/inserts/pyWorkBench.org"
"""
*  /Python Workbench/ ::  [[elisp:(org-cycle)][| ]]  [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
"""
####+END:

####+BEGIN: bx:icm:python:icmItem :itemType "=Imports=   " :itemTitle "*IMPORTS*"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =Imports=    :: *IMPORTS*  [[elisp:(org-cycle)][| ]]
"""
####+END:

import collections
import os
# import shutil
# import invoke
# import tempfile

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/update/sw/icm/py/importUcfIcmBleepG.py"
from unisos import ucf
from unisos import icm

icm.unusedSuppressForEval(ucf.__file__)  # in case icm and ucf are not used

G = icm.IcmGlobalContext()
# G.icmLibsAppend = __file__
# G.icmCmndsLibsAppend = __file__

from blee.icmPlayer import bleep
####+END:

from bisos.currents import bxCurrentsConfig
from bisos.icm import clsMethod

from bisos import bpf

import getpass


####+BEGIN: bx:icm:python:icmItem :itemType "=ImportICMs=" :itemTitle "*Imported Commands Modules*"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =ImportICMs= :: *Imported Commands Modules*  [[elisp:(org-cycle)][| ]]
"""
####+END:

g_importedCmndsModules = [       # Enumerate modules from which CMNDs become invokable
    'blee.icmPlayer.bleep',
]

####+BEGIN: bx:icm:python:func :funcName "commonParamsSpecify" :comment "Params Spec for: --rosu" :funcType "FmWrk" :retType "Void" :deco "" :argsList "icmParams"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-FmWrk :: /commonParamsSpecify/ =Params Spec for: --rosu= retType=Void argsList=(icmParams)  [[elisp:(org-cycle)][| ]]
"""
def commonParamsSpecify(
    icmParams,
):
####+END:
    """
** --rosu (Remote Operations Service Unit. Name of the ROS)
    """
    icmParams.parDictAdd(
        parName='rosu',
        parDescription="Remote Operations Service Unit. Name of the ROS",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        # parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--rosu',
    )

####+BEGIN: bx:icm:python:func :funcName "g_paramsExtraSpecify" :comment "FrameWork: ArgsSpec" :funcType "FmWrk" :retType "Void" :deco "" :argsList "parser"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-FmWrk :: /g_paramsExtraSpecify/ =FrameWork: ArgsSpec= retType=Void argsList=(parser)  [[elisp:(org-cycle)][| ]]
"""
def g_paramsExtraSpecify(
    parser,
):
####+END:
    """
** Module Specific Command Line Parameters.
    g_argsExtraSpecify is passed to G_main and is executed before argsSetup (can not be decorated)
    """
    G = icm.IcmGlobalContext()
    icmParams = icm.ICM_ParamDict()

    bleep.commonParamsSpecify(icmParams)

    clsMethod.commonParamsSpecify(icmParams)  # --cls, --method

    commonParamsSpecify(icmParams)

    icm.argsparseBasedOnIcmParams(parser, icmParams)

    # So that it can be processed later as well.
    G.icmParamDictSet(icmParams)

    return

####+BEGIN: bx:icm:python:icmItem :itemType "=Currents=  " :itemTitle "*Currents -- curBpoId, curSi*"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =Currents=   :: *Currents -- curBpoId, curSi*  [[elisp:(org-cycle)][| ]]
"""
####+END:


####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/update/sw/icm/py/curGetBxOSr.py"
def curGet_bxoId(): return bxCurrentsConfig.bxoId_fpObtain(configBaseDir=None)
def curGet_sr(): return bxCurrentsConfig.sr_fpObtain(configBaseDir=None)
def cmndParsCurBxoSr(cps): cps['bxoId'] = curGet_bxoId(); cps['sr'] = curGet_sr()
####+END:

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "examples" :cmndType "Cmnd-FmWrk"  :comment "FrameWrk: ICM Examples" :parsMand "" :parsOpt "bpoId sivd" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cmnd-FmWrk :: /examples/ =FrameWrk: ICM Examples= parsMand= parsOpt=bpoId sivd argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class examples(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bpoId', 'sivd', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bpoId=None,         # or Cmnd-Input
        sivd=None,         # or Cmnd-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome

            callParamsDict = {'bpoId': bpoId, 'sivd': sivd, }
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome
            bpoId = callParamsDict['bpoId']
            sivd = callParamsDict['sivd']

####+END:
        docStr = """\
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] ICM examples, all on one place.
        """
        if self.docStrClassSet(docStr,): return cmndOutcome

        def cpsInit(): return collections.OrderedDict()
        cmndArgs = "" ; cps=cpsInit() ;
        def menuItem(verbosity='little', comment=""): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity, comment=comment) # 'little' or 'none'
        # def extMenuItem(verbosity): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, icmName=icmExName, verbosity=verbosity) # 'little' or 'none'
        def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)

        #oneBpo = "pmi_ByD-100001"
        #oneBpo = curGet_bxoId()

        #if bpoId: oneBpo = bpoId
        # if si: oneSiRelPath = si

        # logControler = icm.LOG_Control()
        # logControler.loggerSetLevel(20)

        icm.icmExampleMyName(G.icmMyName(), G.icmMyFullName())

        icm.G_commonBriefExamples()

        bleep.examples_icmBasic()

        icm.cmndExampleMenuChapter('*BISOS System (gitSh) Account*')
        execLineEx("""\
bisosAccounts.sh
bisosAccounts.sh -h -v -n showRun -i gitShBxSysAcctVerify  # Info
bisosAccounts.sh -h -v -n showRun -i gitShBxSysAcctCreate  # acctAdd, report
bisosAccounts.sh -h -v -n showRun -i userAcctsDelete gitSh""")

        icm.cmndExampleMenuChapter('*Full Actions*')
        cmndName = "fullServiceUpdate" ; menuItem(verbosity='little')
        cmndName = "fullUserUpdate" ; menuItem(verbosity='little')

        icm.cmndExampleMenuChapter('*Home Account And Keys Setup*')
        cmndName = "gitShAccountCreate" ; menuItem(verbosity='little')
        cmndName = "noInteractiveShellSetup" ; menuItem(verbosity='little')

        icm.cmndExampleMenuChapter('*Invoker (client) Side:: SSH Setup*')
        cmndName = "gitSh_invoker_sshUsgSetup" ; cmndArgs = "localhost" ; menuItem()
        cmndName = "gitSh_invoker_sshUsgSetup" ; cmndArgs = "localhost performerCntnrId" ; menuItem()
        cmndName = "gitSh_invoker_sshUsgLogin" ; cmndArgs = "localhost" ; menuItem()

        icm.cmndExampleMenuChapter('*Performer (server) Side:: SSH Setup*')
        cmndName = "gitSh_performer_sshSetup" ; cmndArgs = "localhost ~/.ssh/id_rsa.pub" ; menuItem(verbosity='little')

        icm.cmndExampleMenuChapter('*Performer (server) Side:: Repos Create And Triggers Setup*')
        cmndName = "gitSh_performer_repo_jekyll" ; cmndArgs = "" ; menuItem(verbosity='little', comment="#create repo in ~gitSh/trigger-jekyll")

        icm.cmndExampleMenuChapter('*Invoker (client) Side:: Trigger With Git Push*')
        cmndName = "gitSh_invoker_repo_jekyll" ; cmndArgs = "/bisos/var/gitSh/invoker" ; menuItem(verbosity='little', comment="# clone baseDir")
        cmndName = "gitSh_invoker_trigger_jekyll" ; cmndArgs = "/bisos/var/gitSh/invoker/trigger-jekyll" ; menuItem(verbosity='little', comment="# repo baseDir")

        return(cmndOutcome)


####+BEGIN: bx:icm:py3:section :title "ICM Commands"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    :: *ICM Commands*  [[elisp:(org-cycle)][| ]]
"""
####+END:


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "fullServiceUpdate" :comment "SERVICE" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /fullServiceUpdate/ =SERVICE= parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class fullServiceUpdate(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome

            callParamsDict = {}
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome

####+END:
        docStr = """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Preformed fullActions, AcctCreat, NonInteractive, ReposCreate
***** TODO Not implemeted yet.
        """
        if self.docStrClassSet(docStr,): return cmndOutcome

        print("AAA")
        print(self.docStrClass())

        return cmndOutcome.set(
            opError=icm.OpError.Success,  # type: ignore
            opResults=None,
        )


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "fullUserUpdate" :comment "USER" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /fullUserUpdate/ =USER= parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class fullUserUpdate(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome

            callParamsDict = {}
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome

####+END:
        docStr = """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Preformed fullActions, AcctCreat, NonInteractive, ReposCreate
***** TODO Not implemeted yet.
        """
        if self.docStrClassSet(docStr,): return cmndOutcome

        print("AAA")
        print(self.docStrClass())

        return cmndOutcome.set(
            opError=icm.OpError.Success,  # type: ignore
            opResults=None,
        )


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "gitShAccountCreate" :comment "SERVICE" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /gitShAccountCreate/ =SERVICE= parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class gitShAccountCreate(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome

            callParamsDict = {}
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome

####+END:
        docStr = """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Create the account using _bisosAccounts.sh_
        """
        if self.docStrClassSet(docStr,): return cmndOutcome

        shIcmComOpts = bpf.shIcm.comOpts(self)

        if not bpf.subProc.WOpW(invedBy=self,).bash(
                f"""bisosAccounts.sh {shIcmComOpts} -i gitShBxSysAcctVerify""",
        ).exitCode():
            icm.LOG_here("gitSh acct is in place -- creation skipped")
        else:
            if bpf.subProc.WOpW(invedBy=self,).bash(
                f"""bisosAccounts.sh {shIcmComOpts} -i gitShBxSysAcctCreate""",
            ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        return icm.opSuccessAnNoResult(cmndOutcome)


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "noInteractiveShellSetup" :comment "SERVICE" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /noInteractiveShellSetup/ =SERVICE= parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class noInteractiveShellSetup(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome

            callParamsDict = {}
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome

####+END:
        docStr = """\
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Create ~gitSh/git-shell-commands if needed
***** TODO For now this is a bash translation. Needs to be done in pure python.
        """
        if self.docStrClassSet(docStr,): return cmndOutcome

        gitShCommandsBaseDir = os.path.join(
            os.path.expanduser("~gitSh"),
            "git-shell-commands",
        )
        if os.path.isdir(gitShCommandsBaseDir):
            icm.LOG_here(f"{gitShCommandsBaseDir} is in place -- creation skipped")
        else:
            bpf.subProc.WOpW(invedBy=self,).bash(
                f"""sudo -u gitSh  mkdir {gitShCommandsBaseDir}""",
            )

        noInteractiveLoginFileContent = """\
#!/usr/bin/env bash

printf '%s\\n' "Authenticated as $USER user, but interactive logins are disabled."

exit 128
"""
        gitShNoInteractiveLogingPath = os.path.join(
            gitShCommandsBaseDir,
            "no-interactive-login",
        )
        bpf.pyRunAs.as_gitSh_writeToFile(
            gitShNoInteractiveLogingPath,
            noInteractiveLoginFileContent,
        )
        bpf.subProc.WOpW(invedBy=self,).bash(
            f"""sudo -u gitSh chmod +x {gitShNoInteractiveLogingPath}""",
        )
        print(
            bpf.subProc.WOpW(invedBy=self,).bash(
                f"""ls -l {gitShNoInteractiveLogingPath}""",
            ).stdout
        )

        return icm.opSuccessAnNoResult(cmndOutcome)

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "gitSh_invoker_sshUsgSetup" :comment "USER" :parsMand "" :parsOpt "" :argsMin "1" :argsMax "9999" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /gitSh_invoker_sshUsgSetup/ =USER= parsMand= parsOpt= argsMin=1 argsMax=9999 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class gitSh_invoker_sshUsgSetup(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 9999,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome
                effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
            else:
                effectiveArgsList = argsList

            callParamsDict = {}
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome

            cmndArgsSpecDict = self.cmndArgsSpec()
            if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
                return cmndOutcome
####+END:
        docStr = """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Create an entry for each specified triggerable service container.
***** Process each arg as a performer cntnrId  using usgBpoSshCustomManage.sh. Adds to ~/.ssh/config.
        """
        if self.docStrClassSet(docStr,): return cmndOutcome

        curUser = getpass.getuser()

        curUserSshPrivKeyFile = os.path.join(
            os.path.expanduser("~"),
            ".ssh",
            "id_rsa",
        )

        shIcmComOpts = bpf.shIcm.comOpts(self)

        for each in effectiveArgsList:  # type: ignore
            gitSshLabel = f"gitSh-{each}"
            if bpf.subProc.WOpW(invedBy=self,).bash(
                f"""usgBpoSshCustomManage.sh {shIcmComOpts} -p usg={curUser} -i usgCustomFullUpdate {gitSshLabel} {curUserSshPrivKeyFile} {each}  gitSh 22""",
            ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        return icm.opSuccessAnNoResult(cmndOutcome)

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
***** Cmnd Args Specification: process each as any cntnr -- 0&9999
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&9999",
            argName="cntnrs",
            argDefault='localhost',
            argChoices='any',
            argDescription="Process Each",
        )

        return cmndArgsSpecDict



####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "gitSh_invoker_sshUsgLogin" :comment "USER" :parsMand "" :parsOpt "" :argsMin "1" :argsMax "9999" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /gitSh_invoker_sshUsgLogin/ =USER= parsMand= parsOpt= argsMin=1 argsMax=9999 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class gitSh_invoker_sshUsgLogin(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 9999,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome
                effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
            else:
                effectiveArgsList = argsList

            callParamsDict = {}
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome

            cmndArgsSpecDict = self.cmndArgsSpec()
            if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
                return cmndOutcome
####+END:
        docStr = """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Login to each container.
***** For each, there should be no password prompt. But login should be declined.
        """
        if self.docStrClassSet(docStr,): return cmndOutcome

        for each in effectiveArgsList:  # type: ignore
            gitSshLabel = f"gitSh-{each}"
            bpf.subProc.WOpW(invedBy=self,).bash(
                f"""ssh {gitSshLabel}""",
            )

        return icm.opSuccessAnNoResult(cmndOutcome)

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
***** Cmnd Args Specification: process each as any cntnr -- 0&9999
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&9999",
            argName="cntnrs",
            argDefault='localhost',
            argChoices='any',
            argDescription="Process Each",
        )

        return cmndArgsSpecDict


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "gitSh_performer_sshSetup" :comment "SERVICE" :parsMand "" :parsOpt "" :argsMin "2" :argsMax "2" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /gitSh_performer_sshSetup/ =SERVICE= parsMand= parsOpt= argsMin=2 argsMax=2 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class gitSh_performer_sshSetup(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 2, 'Max': 2,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome
                effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
            else:
                effectiveArgsList = argsList

            callParamsDict = {}
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome

            cmndArgsSpecDict = self.cmndArgsSpec()
            if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
                return cmndOutcome
####+END:
        docStr = """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] NOTYET_
***** arg1 is cntnrName, arg2 is pubKeyFile.
***** Add pub key to authorized file. Change permissions.
        """
        if self.docStrClassSet(docStr,): return cmndOutcome

        cntnrName = effectiveArgsList[0]  # type: ignore
        pubKeyFile = effectiveArgsList[1]  # type: ignore
        #

        if cntnrName != "localhost":
            print("Unimplemented")
            return icm.opSuccessAnNoResult(cmndOutcome)

        gitShAuthorizedFile = os.path.join(
            os.path.expanduser("~gitSh"),
            ".ssh",
            "authorized_keys",
        )

        with open(pubKeyFile, 'r') as file:
            pubKeyAsStr = file.read().rstrip()

        if not bpf.subProc.WOpW(invedBy=self,).bash(
                f"""sudo -u gitSh grep "{pubKeyAsStr}" {gitShAuthorizedFile}""",
        ).exitCode():
            icm.LOG_here(f"pubKey already in {gitShAuthorizedFile}")
            return icm.opSuccessAnNoResult(cmndOutcome)

        if bpf.subProc.WOpW(invedBy=self,).bash(
                f"""cat {pubKeyFile} | sudo -u gitSh tee -a {gitShAuthorizedFile}""",
        ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        if bpf.subProc.WOpW(invedBy=self,).bash(
            f"""sudo -u gitSh chmod go-w {gitShAuthorizedFile}""",
        ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))
        print(
            bpf.subProc.WOpW(invedBy=self,).bash(
                f"""sudo -u gitSh ls -l {gitShAuthorizedFile}""",
            ).stdout
        )

        return icm.opSuccessAnNoResult(cmndOutcome)


####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
***** Cmnd Args Specification: cntnr and pubKey
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="cntnr",
            argDefault='localhost',
            argChoices='any',
            argDescription="Container to which pubKey will be added.",
        )
        cmndArgsSpecDict.argsDictAdd(
            argPosition="1",
            argName="pubKey",
            argDefault='~gitSh/.ssh/id_rsa.pub',
            argChoices='any',
            argDescription="pubKey to be added to cntnr.",
        )
        return cmndArgsSpecDict

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "gitSh_performer_rosu_repoCreate" :comment "SERVICE" :parsMand "rosu" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /gitSh_performer_rosu_repoCreate/ =SERVICE= parsMand=rosu parsOpt= argsMin=1 argsMax=1 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class gitSh_performer_rosu_repoCreate(icm.Cmnd):
    cmndParamsMandatory = [ 'rosu', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        rosu=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome
                effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
            else:
                effectiveArgsList = argsList

            callParamsDict = {'rosu': rosu, }
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome
            rosu = callParamsDict['rosu']

            cmndArgsSpecDict = self.cmndArgsSpec()
            if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
                return cmndOutcome
####+END:
        docStr = """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Create the repo named rosu, if it does not exist.
***** Repo Create; Create post-./post-receive
        """
        if self.docStrClassSet(docStr,): return cmndOutcome

        repoName = f"{rosu}.git"

        repoBaseDir = os.path.join(
            os.path.expanduser("~gitSh"),
            repoName,
        )
        if os.path.isdir(repoBaseDir):
            icm.LOG_here(f"{repoBaseDir} is in place -- creation skipped")
            return icm.opSuccessAnNoResult(cmndOutcome)
        else:
            if bpf.subProc.WOpW(invedBy=self,).bash(
                f"""sudo -u gitSh mkdir {repoBaseDir}""",
            ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

            if bpf.subProc.WOpW(invedBy=self, cd=repoBaseDir).bash(
                    f"""sudo -u gitSh git init --bare""",
            ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        #
        # NOTYET, Cleanup sammy ...
        #
        postReceiveHookContent = """\
#!/usr/bin/env bash

#
# General purpose operations dispatch
#

GIT_REPO=$HOME/sammy-blog.git
TMP_GIT_CLONE=/tmp/sammy-blog
PUBLIC_WWW=/var/www/html

dateTag=$(date +%y%m%d%H%M%S)

echo ${TMP_GIT_CLONE} > /tmp/trigger.${dateTag}

exit
"""
        postReceiveHookPath = os.path.join(
            repoBaseDir,
            "hooks",
            "post-receive",
        )
        bpf.pyRunAs.as_gitSh_writeToFile(
            postReceiveHookPath,
            postReceiveHookContent,
        )
        bpf.subProc.WOpW(invedBy=self,).bash(
            f"""sudo -u gitSh chmod +x {postReceiveHookPath}""",
        )
        print(
            bpf.subProc.WOpW(invedBy=self,).bash(
                f"""ls -l {postReceiveHookPath}""",
            ).stdout
        )

        return icm.opSuccessAnNoResult(cmndOutcome)

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "gitSh_performer_repo_jekyll" :comment "SERVICE" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /gitSh_performer_repo_jekyll/ =SERVICE= parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class gitSh_performer_repo_jekyll(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome

            callParamsDict = {}
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome

####+END:
        docStr = """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] NOTYET_
***** Repo Create; Create post-./post-receive
        """
        if self.docStrClassSet(docStr,): return cmndOutcome

        triggerJekyllRepoName = "trigger-jekyll.git"

        triggerJekyllRepoBaseDir = os.path.join(
            os.path.expanduser("~gitSh"),
            triggerJekyllRepoName,
        )
        if os.path.isdir(triggerJekyllRepoBaseDir):
            icm.LOG_here(f"{triggerJekyllRepoBaseDir} is in place -- creation skipped")
            return icm.opSuccessAnNoResult(cmndOutcome)
        else:
            if bpf.subProc.WOpW(invedBy=self,).bash(
                f"""sudo -u gitSh mkdir {triggerJekyllRepoBaseDir}""",
            ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        if bpf.subProc.WOpW(invedBy=self, cd=triggerJekyllRepoBaseDir).bash(
                f"""sudo -u gitSh git init --bare""",
        ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        #
        # NOTYET, Cleanup sammy ...
        #
        postReceiveHookContent = """\
#!/usr/bin/env bash

GIT_REPO=$HOME/sammy-blog.git
TMP_GIT_CLONE=/tmp/sammy-blog
PUBLIC_WWW=/var/www/html


dateTag=$(date +%y%m%d%H%M%S)

echo ${TMP_GIT_CLONE} > /tmp/trigger.${dateTag}

exit
"""
        postReceiveHookPath = os.path.join(
            triggerJekyllRepoBaseDir,
            "hooks",
            "post-receive",
        )
        bpf.pyRunAs.as_gitSh_writeToFile(
            postReceiveHookPath,
            postReceiveHookContent,
        )
        bpf.subProc.WOpW(invedBy=self,).bash(
            f"""sudo -u gitSh chmod +x {postReceiveHookPath}""",
        )
        print(
            bpf.subProc.WOpW(invedBy=self,).bash(
                f"""ls -l {postReceiveHookPath}""",
            ).stdout
        )

        return icm.opSuccessAnNoResult(cmndOutcome)


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "gitSh_invoker_rosu_repoClone" :comment "USER" :parsMand "rosu" :parsOpt "" :argsMin "0" :argsMax "2" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /gitSh_invoker_rosu_repoClone/ =USER= parsMand=rosu parsOpt= argsMin=0 argsMax=2 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class gitSh_invoker_rosu_repoClone(icm.Cmnd):
    cmndParamsMandatory = [ 'rosu', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 2,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        rosu=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome
                effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
            else:
                effectiveArgsList = argsList

            callParamsDict = {'rosu': rosu, }
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome
            rosu = callParamsDict['rosu']

            cmndArgsSpecDict = self.cmndArgsSpec()
            if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
                return cmndOutcome
####+END:
        docStr = """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Use arg0 and param rosu to clone
***** update file. add .; commit; push
        """
        if self.docStrClassSet(docStr,): return cmndOutcome

        cmndArg0 = self.cmndArgsGet("0", cmndArgsSpecDict, effectiveArgsList) # type: ignore
        repoBase = cmndArg0  # type: ignore

        if not os.path.isdir(repoBase):
            return(icm.EH_badOutcome(cmndOutcome))

        repoName = rosu

        if os.path.isdir(os.path.join(repoBase, repoName)):
            icm.LOG_here(f"{os.path.join(repoBase, repoName)} is in place -- git-cloning skipped")
            return icm.opSuccessAnNoResult(cmndOutcome)

        if bpf.subProc.WOpW(invedBy=self, cd=repoBase).bash(
                f"""git clone gitSh@gitSh-localhost:{rosu}.git""",
        ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        return icm.opSuccessAnNoResult(cmndOutcome)


####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
***** Cmnd Args Specification: cntnr and pubKey
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="repoBase",
            argDefault='/bisos/var/gitSh/invoker',
            argChoices='any',
            argDescription="Base dir in which repo will be cloned.",
        )

        return cmndArgsSpecDict



####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "gitSh_invoker_repo_jekyll" :comment "USER" :parsMand "" :parsOpt "" :argsMin "1" :argsMax "1" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /gitSh_invoker_repo_jekyll/ =USER= parsMand= parsOpt= argsMin=1 argsMax=1 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class gitSh_invoker_repo_jekyll(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome
                effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
            else:
                effectiveArgsList = argsList

            callParamsDict = {}
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome

            cmndArgsSpecDict = self.cmndArgsSpec()
            if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
                return cmndOutcome
####+END:
        docStr = """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] NOTYET_
***** update file. add .; commit; push
        """
        if self.docStrClassSet(docStr,): return cmndOutcome

        repoBase = effectiveArgsList[0]  # type: ignore

        if not os.path.isdir(repoBase):
            return(icm.EH_badOutcome(cmndOutcome))

        triggerJekyllRepoName = "trigger-jekyll.git"

        if os.path.isdir(os.path.join(repoBase, triggerJekyllRepoName)):
            icm.LOG_here(f"{os.path.join(repoBase, triggerJekyllRepoName)} is in place -- creation skipped")
            return icm.opSuccessAnNoResult(cmndOutcome)

        if bpf.subProc.WOpW(invedBy=self, cd=repoBase).bash(
                f"""git clone gitSh@gitSh-localhost:trigger-jekyll.git""",
        ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        return icm.opSuccessAnNoResult(cmndOutcome)


####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
***** Cmnd Args Specification: cntnr and pubKey
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="repoBase",
            argDefault='/tmp',
            argChoices='any',
            argDescription="Base dir in which repo will be created.",
        )
        return cmndArgsSpecDict


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "gitSh_inv_opAP_create" :comment "USER" :parsMand "rosu" :parsOpt "" :argsMin "1" :argsMax "1" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /gitSh_inv_opAP_create/ =USER= parsMand=rosu parsOpt= argsMin=1 argsMax=1 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class gitSh_inv_opAP_create(icm.Cmnd):
    cmndParamsMandatory = [ 'rosu', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        rosu=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome
                effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
            else:
                effectiveArgsList = argsList

            callParamsDict = {'rosu': rosu, }
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome
            rosu = callParamsDict['rosu']

            cmndArgsSpecDict = self.cmndArgsSpec()
            if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
                return cmndOutcome
####+END:
        docStr = """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Creates an invokation Access Point
***** update file. add .; commit; push
        """
        if self.docStrClassSet(docStr,): return cmndOutcome

        repoBase = effectiveArgsList[0]  # type: ignore

        if not os.path.isdir(repoBase):
            icm.EH_problem_usageError(f"Missing {repoBase}")
            return(icm.EH_badOutcome(cmndOutcome))

        if bpf.subProc.WOpW(invedBy=self, cd=repoBase).bash(
                f"""date | tee -a oneFile""",
        ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        if bpf.subProc.WOpW(invedBy=self, cd=repoBase).bash(
                f"""git add .""",
        ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        if bpf.subProc.WOpW(invedBy=self, cd=repoBase).bash(
                f"""git commit -m "Auto Generated." """,
        ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        if bpf.subProc.WOpW(invedBy=self, cd=repoBase).bash(
                f"""git push""",
        ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        return icm.opSuccessAnNoResult(cmndOutcome)


####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
***** Cmnd Args Specification: cntnr and pubKey
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="repoBase",
            argDefault='/tmp/trigger-jekyll',
            argChoices='any',
            argDescription="Base dir in which repo will be created.",
        )
        cmndArgsSpecDict.argsDictAdd(
            argPosition="1",
            argName="palsId",
            argDefault='thisPalsId',
            argChoices='any',
            argDescription="Base dir in which repo will be created.",
        )
        return cmndArgsSpecDict



####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "gitSh_invoker_trigger_jekyll" :comment "USER" :parsMand "" :parsOpt "" :argsMin "1" :argsMax "1" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /gitSh_invoker_trigger_jekyll/ =USER= parsMand= parsOpt= argsMin=1 argsMax=1 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class gitSh_invoker_trigger_jekyll(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome
                effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
            else:
                effectiveArgsList = argsList

            callParamsDict = {}
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome

            cmndArgsSpecDict = self.cmndArgsSpec()
            if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
                return cmndOutcome
####+END:
        docStr = """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] NOTYET_
***** update file. add .; commit; push
        """
        if self.docStrClassSet(docStr,): return cmndOutcome

        repoBase = effectiveArgsList[0]  # type: ignore

        if not os.path.isdir(repoBase):
            icm.EH_problem_usageError(f"Missing {repoBase}")
            return(icm.EH_badOutcome(cmndOutcome))

        if bpf.subProc.WOpW(invedBy=self, cd=repoBase).bash(
                f"""date | tee -a oneFile""",
        ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        if bpf.subProc.WOpW(invedBy=self, cd=repoBase).bash(
                f"""git add .""",
        ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        if bpf.subProc.WOpW(invedBy=self, cd=repoBase).bash(
                f"""git commit -m "Auto Generated." """,
        ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        if bpf.subProc.WOpW(invedBy=self, cd=repoBase).bash(
                f"""git push""",
        ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        return icm.opSuccessAnNoResult(cmndOutcome)


####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
***** Cmnd Args Specification: cntnr and pubKey
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="repoBase",
            argDefault='/tmp/trigger-jekyll',
            argChoices='any',
            argDescription="Base dir in which repo will be created.",
        )
        cmndArgsSpecDict.argsDictAdd(
            argPosition="1",
            argName="palsId",
            argDefault='thisPalsId',
            argChoices='any',
            argDescription="Base dir in which repo will be created.",
        )
        return cmndArgsSpecDict


####+BEGIN: bx:icm:py3:section :title "Supporting Classes And Functions"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    :: *Supporting Classes And Functions*  [[elisp:(org-cycle)][| ]]
"""
####+END:
"""
*       /Empty/  [[elisp:(org-cycle)][| ]]
"""

####+BEGIN: bx:icm:py3:section :title "Common/Generic Facilities -- Library Candidates"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    :: *Common/Generic Facilities -- Library Candidates*  [[elisp:(org-cycle)][| ]]
"""
####+END:
"""
*       /Empty/  [[elisp:(org-cycle)][| ]]
"""

####+BEGIN: bx:icm:py3:main :mainType  "withExamples" :comment "Common"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =Framework=  ::   __main__ g_icmMain :: /withExamples/ =Common=  [[elisp:(org-cycle)][| ]]
"""
#
# ICM Main Type is: withExamples
#
if __name__ == "__main__":
    icm.g_icmMain(
        icmInfo=icmInfo,
        noCmndEntry=examples, # noCmndEntry=mainEntry,
        extraParamsHook=g_paramsExtraSpecify,
        importedCmndsModules=g_importedCmndsModules,
    )

####+END:

####+BEGINNOT: bx:icm:py3:section :title "Unused Facilities -- Temporary Junk Yard"
"""
* +
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    :: *Unused Facilities -- Temporary Junk Yard*  [[elisp:(org-cycle)][| ]]
"""
####+END:
"""
*       /Empty/  [[elisp:(org-cycle)][| ]]
"""

####+BEGIN: bx:icm:py3:section :title "End Of Editable Text"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    :: *End Of Editable Text*  [[elisp:(org-cycle)][| ]]
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
