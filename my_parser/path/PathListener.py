# Generated from Path.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PathParser import PathParser
else:
    from PathParser import PathParser

# This class defines a complete listener for a parse tree produced by PathParser.
class PathListener(ParseTreeListener):

    # Enter a parse tree produced by PathParser#path.
    def enterPath(self, ctx:PathParser.PathContext):
        pass

    # Exit a parse tree produced by PathParser#path.
    def exitPath(self, ctx:PathParser.PathContext):
        pass


    # Enter a parse tree produced by PathParser#p_value.
    def enterP_value(self, ctx:PathParser.P_valueContext):
        pass

    # Exit a parse tree produced by PathParser#p_value.
    def exitP_value(self, ctx:PathParser.P_valueContext):
        pass


    # Enter a parse tree produced by PathParser#value.
    def enterValue(self, ctx:PathParser.ValueContext):
        pass

    # Exit a parse tree produced by PathParser#value.
    def exitValue(self, ctx:PathParser.ValueContext):
        pass


    # Enter a parse tree produced by PathParser#ilg.
    def enterIlg(self, ctx:PathParser.IlgContext):
        pass

    # Exit a parse tree produced by PathParser#ilg.
    def exitIlg(self, ctx:PathParser.IlgContext):
        pass


    # Enter a parse tree produced by PathParser#label.
    def enterLabel(self, ctx:PathParser.LabelContext):
        pass

    # Exit a parse tree produced by PathParser#label.
    def exitLabel(self, ctx:PathParser.LabelContext):
        pass


    # Enter a parse tree produced by PathParser#delim.
    def enterDelim(self, ctx:PathParser.DelimContext):
        pass

    # Exit a parse tree produced by PathParser#delim.
    def exitDelim(self, ctx:PathParser.DelimContext):
        pass


    # Enter a parse tree produced by PathParser#ch_ilg.
    def enterCh_ilg(self, ctx:PathParser.Ch_ilgContext):
        pass

    # Exit a parse tree produced by PathParser#ch_ilg.
    def exitCh_ilg(self, ctx:PathParser.Ch_ilgContext):
        pass


    # Enter a parse tree produced by PathParser#ldse.
    def enterLdse(self, ctx:PathParser.LdseContext):
        pass

    # Exit a parse tree produced by PathParser#ldse.
    def exitLdse(self, ctx:PathParser.LdseContext):
        pass


    # Enter a parse tree produced by PathParser#opNot.
    def enterOpNot(self, ctx:PathParser.OpNotContext):
        pass

    # Exit a parse tree produced by PathParser#opNot.
    def exitOpNot(self, ctx:PathParser.OpNotContext):
        pass


    # Enter a parse tree produced by PathParser#opBinInvert.
    def enterOpBinInvert(self, ctx:PathParser.OpBinInvertContext):
        pass

    # Exit a parse tree produced by PathParser#opBinInvert.
    def exitOpBinInvert(self, ctx:PathParser.OpBinInvertContext):
        pass


    # Enter a parse tree produced by PathParser#opEqual.
    def enterOpEqual(self, ctx:PathParser.OpEqualContext):
        pass

    # Exit a parse tree produced by PathParser#opEqual.
    def exitOpEqual(self, ctx:PathParser.OpEqualContext):
        pass


    # Enter a parse tree produced by PathParser#opLt.
    def enterOpLt(self, ctx:PathParser.OpLtContext):
        pass

    # Exit a parse tree produced by PathParser#opLt.
    def exitOpLt(self, ctx:PathParser.OpLtContext):
        pass


    # Enter a parse tree produced by PathParser#opGt.
    def enterOpGt(self, ctx:PathParser.OpGtContext):
        pass

    # Exit a parse tree produced by PathParser#opGt.
    def exitOpGt(self, ctx:PathParser.OpGtContext):
        pass


    # Enter a parse tree produced by PathParser#opMinus.
    def enterOpMinus(self, ctx:PathParser.OpMinusContext):
        pass

    # Exit a parse tree produced by PathParser#opMinus.
    def exitOpMinus(self, ctx:PathParser.OpMinusContext):
        pass


    # Enter a parse tree produced by PathParser#opSem.
    def enterOpSem(self, ctx:PathParser.OpSemContext):
        pass

    # Exit a parse tree produced by PathParser#opSem.
    def exitOpSem(self, ctx:PathParser.OpSemContext):
        pass


    # Enter a parse tree produced by PathParser#cmt.
    def enterCmt(self, ctx:PathParser.CmtContext):
        pass

    # Exit a parse tree produced by PathParser#cmt.
    def exitCmt(self, ctx:PathParser.CmtContext):
        pass


    # Enter a parse tree produced by PathParser#ddash.
    def enterDdash(self, ctx:PathParser.DdashContext):
        pass

    # Exit a parse tree produced by PathParser#ddash.
    def exitDdash(self, ctx:PathParser.DdashContext):
        pass


    # Enter a parse tree produced by PathParser#quote.
    def enterQuote(self, ctx:PathParser.QuoteContext):
        pass

    # Exit a parse tree produced by PathParser#quote.
    def exitQuote(self, ctx:PathParser.QuoteContext):
        pass


    # Enter a parse tree produced by PathParser#dquote.
    def enterDquote(self, ctx:PathParser.DquoteContext):
        pass

    # Exit a parse tree produced by PathParser#dquote.
    def exitDquote(self, ctx:PathParser.DquoteContext):
        pass


    # Enter a parse tree produced by PathParser#us_sgn.
    def enterUs_sgn(self, ctx:PathParser.Us_sgnContext):
        pass

    # Exit a parse tree produced by PathParser#us_sgn.
    def exitUs_sgn(self, ctx:PathParser.Us_sgnContext):
        pass


    # Enter a parse tree produced by PathParser#c_and.
    def enterC_and(self, ctx:PathParser.C_andContext):
        pass

    # Exit a parse tree produced by PathParser#c_and.
    def exitC_and(self, ctx:PathParser.C_andContext):
        pass


    # Enter a parse tree produced by PathParser#c_or.
    def enterC_or(self, ctx:PathParser.C_orContext):
        pass

    # Exit a parse tree produced by PathParser#c_or.
    def exitC_or(self, ctx:PathParser.C_orContext):
        pass


    # Enter a parse tree produced by PathParser#c_slash.
    def enterC_slash(self, ctx:PathParser.C_slashContext):
        pass

    # Exit a parse tree produced by PathParser#c_slash.
    def exitC_slash(self, ctx:PathParser.C_slashContext):
        pass


    # Enter a parse tree produced by PathParser#c_slash_hex.
    def enterC_slash_hex(self, ctx:PathParser.C_slash_hexContext):
        pass

    # Exit a parse tree produced by PathParser#c_slash_hex.
    def exitC_slash_hex(self, ctx:PathParser.C_slash_hexContext):
        pass


    # Enter a parse tree produced by PathParser#c_dot.
    def enterC_dot(self, ctx:PathParser.C_dotContext):
        pass

    # Exit a parse tree produced by PathParser#c_dot.
    def exitC_dot(self, ctx:PathParser.C_dotContext):
        pass


    # Enter a parse tree produced by PathParser#c_colon.
    def enterC_colon(self, ctx:PathParser.C_colonContext):
        pass

    # Exit a parse tree produced by PathParser#c_colon.
    def exitC_colon(self, ctx:PathParser.C_colonContext):
        pass


    # Enter a parse tree produced by PathParser#s_bslash.
    def enterS_bslash(self, ctx:PathParser.S_bslashContext):
        pass

    # Exit a parse tree produced by PathParser#s_bslash.
    def exitS_bslash(self, ctx:PathParser.S_bslashContext):
        pass


    # Enter a parse tree produced by PathParser#c_q.
    def enterC_q(self, ctx:PathParser.C_qContext):
        pass

    # Exit a parse tree produced by PathParser#c_q.
    def exitC_q(self, ctx:PathParser.C_qContext):
        pass


    # Enter a parse tree produced by PathParser#par_open.
    def enterPar_open(self, ctx:PathParser.Par_openContext):
        pass

    # Exit a parse tree produced by PathParser#par_open.
    def exitPar_open(self, ctx:PathParser.Par_openContext):
        pass


    # Enter a parse tree produced by PathParser#par_close.
    def enterPar_close(self, ctx:PathParser.Par_closeContext):
        pass

    # Exit a parse tree produced by PathParser#par_close.
    def exitPar_close(self, ctx:PathParser.Par_closeContext):
        pass


    # Enter a parse tree produced by PathParser#c_star.
    def enterC_star(self, ctx:PathParser.C_starContext):
        pass

    # Exit a parse tree produced by PathParser#c_star.
    def exitC_star(self, ctx:PathParser.C_starContext):
        pass


    # Enter a parse tree produced by PathParser#c_percent.
    def enterC_percent(self, ctx:PathParser.C_percentContext):
        pass

    # Exit a parse tree produced by PathParser#c_percent.
    def exitC_percent(self, ctx:PathParser.C_percentContext):
        pass


    # Enter a parse tree produced by PathParser#c_brack.
    def enterC_brack(self, ctx:PathParser.C_brackContext):
        pass

    # Exit a parse tree produced by PathParser#c_brack.
    def exitC_brack(self, ctx:PathParser.C_brackContext):
        pass


    # Enter a parse tree produced by PathParser#c_acolad.
    def enterC_acolad(self, ctx:PathParser.C_acoladContext):
        pass

    # Exit a parse tree produced by PathParser#c_acolad.
    def exitC_acolad(self, ctx:PathParser.C_acoladContext):
        pass


    # Enter a parse tree produced by PathParser#c_dollar.
    def enterC_dollar(self, ctx:PathParser.C_dollarContext):
        pass

    # Exit a parse tree produced by PathParser#c_dollar.
    def exitC_dollar(self, ctx:PathParser.C_dollarContext):
        pass


    # Enter a parse tree produced by PathParser#c_adsgn.
    def enterC_adsgn(self, ctx:PathParser.C_adsgnContext):
        pass

    # Exit a parse tree produced by PathParser#c_adsgn.
    def exitC_adsgn(self, ctx:PathParser.C_adsgnContext):
        pass


    # Enter a parse tree produced by PathParser#c_irg1.
    def enterC_irg1(self, ctx:PathParser.C_irg1Context):
        pass

    # Exit a parse tree produced by PathParser#c_irg1.
    def exitC_irg1(self, ctx:PathParser.C_irg1Context):
        pass



del PathParser