# Generated from Query.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .QueryParser import QueryParser
else:
    from QueryParser import QueryParser

# This class defines a complete listener for a parse tree produced by QueryParser.
class QueryListener(ParseTreeListener):

    # Enter a parse tree produced by QueryParser#query.
    def enterQuery(self, ctx:QueryParser.QueryContext):
        pass

    # Exit a parse tree produced by QueryParser#query.
    def exitQuery(self, ctx:QueryParser.QueryContext):
        pass


    # Enter a parse tree produced by QueryParser#p_id.
    def enterP_id(self, ctx:QueryParser.P_idContext):
        pass

    # Exit a parse tree produced by QueryParser#p_id.
    def exitP_id(self, ctx:QueryParser.P_idContext):
        pass


    # Enter a parse tree produced by QueryParser#q_value.
    def enterQ_value(self, ctx:QueryParser.Q_valueContext):
        pass

    # Exit a parse tree produced by QueryParser#q_value.
    def exitQ_value(self, ctx:QueryParser.Q_valueContext):
        pass


    # Enter a parse tree produced by QueryParser#value.
    def enterValue(self, ctx:QueryParser.ValueContext):
        pass

    # Exit a parse tree produced by QueryParser#value.
    def exitValue(self, ctx:QueryParser.ValueContext):
        pass


    # Enter a parse tree produced by QueryParser#ilg.
    def enterIlg(self, ctx:QueryParser.IlgContext):
        pass

    # Exit a parse tree produced by QueryParser#ilg.
    def exitIlg(self, ctx:QueryParser.IlgContext):
        pass


    # Enter a parse tree produced by QueryParser#label.
    def enterLabel(self, ctx:QueryParser.LabelContext):
        pass

    # Exit a parse tree produced by QueryParser#label.
    def exitLabel(self, ctx:QueryParser.LabelContext):
        pass


    # Enter a parse tree produced by QueryParser#delim.
    def enterDelim(self, ctx:QueryParser.DelimContext):
        pass

    # Exit a parse tree produced by QueryParser#delim.
    def exitDelim(self, ctx:QueryParser.DelimContext):
        pass


    # Enter a parse tree produced by QueryParser#ch_ilg.
    def enterCh_ilg(self, ctx:QueryParser.Ch_ilgContext):
        pass

    # Exit a parse tree produced by QueryParser#ch_ilg.
    def exitCh_ilg(self, ctx:QueryParser.Ch_ilgContext):
        pass


    # Enter a parse tree produced by QueryParser#ldse.
    def enterLdse(self, ctx:QueryParser.LdseContext):
        pass

    # Exit a parse tree produced by QueryParser#ldse.
    def exitLdse(self, ctx:QueryParser.LdseContext):
        pass


    # Enter a parse tree produced by QueryParser#opNot.
    def enterOpNot(self, ctx:QueryParser.OpNotContext):
        pass

    # Exit a parse tree produced by QueryParser#opNot.
    def exitOpNot(self, ctx:QueryParser.OpNotContext):
        pass


    # Enter a parse tree produced by QueryParser#opBinInvert.
    def enterOpBinInvert(self, ctx:QueryParser.OpBinInvertContext):
        pass

    # Exit a parse tree produced by QueryParser#opBinInvert.
    def exitOpBinInvert(self, ctx:QueryParser.OpBinInvertContext):
        pass


    # Enter a parse tree produced by QueryParser#opEqual.
    def enterOpEqual(self, ctx:QueryParser.OpEqualContext):
        pass

    # Exit a parse tree produced by QueryParser#opEqual.
    def exitOpEqual(self, ctx:QueryParser.OpEqualContext):
        pass


    # Enter a parse tree produced by QueryParser#opLt.
    def enterOpLt(self, ctx:QueryParser.OpLtContext):
        pass

    # Exit a parse tree produced by QueryParser#opLt.
    def exitOpLt(self, ctx:QueryParser.OpLtContext):
        pass


    # Enter a parse tree produced by QueryParser#opGt.
    def enterOpGt(self, ctx:QueryParser.OpGtContext):
        pass

    # Exit a parse tree produced by QueryParser#opGt.
    def exitOpGt(self, ctx:QueryParser.OpGtContext):
        pass


    # Enter a parse tree produced by QueryParser#opMinus.
    def enterOpMinus(self, ctx:QueryParser.OpMinusContext):
        pass

    # Exit a parse tree produced by QueryParser#opMinus.
    def exitOpMinus(self, ctx:QueryParser.OpMinusContext):
        pass


    # Enter a parse tree produced by QueryParser#opSem.
    def enterOpSem(self, ctx:QueryParser.OpSemContext):
        pass

    # Exit a parse tree produced by QueryParser#opSem.
    def exitOpSem(self, ctx:QueryParser.OpSemContext):
        pass


    # Enter a parse tree produced by QueryParser#cmt.
    def enterCmt(self, ctx:QueryParser.CmtContext):
        pass

    # Exit a parse tree produced by QueryParser#cmt.
    def exitCmt(self, ctx:QueryParser.CmtContext):
        pass


    # Enter a parse tree produced by QueryParser#ddash.
    def enterDdash(self, ctx:QueryParser.DdashContext):
        pass

    # Exit a parse tree produced by QueryParser#ddash.
    def exitDdash(self, ctx:QueryParser.DdashContext):
        pass


    # Enter a parse tree produced by QueryParser#quote.
    def enterQuote(self, ctx:QueryParser.QuoteContext):
        pass

    # Exit a parse tree produced by QueryParser#quote.
    def exitQuote(self, ctx:QueryParser.QuoteContext):
        pass


    # Enter a parse tree produced by QueryParser#dquote.
    def enterDquote(self, ctx:QueryParser.DquoteContext):
        pass

    # Exit a parse tree produced by QueryParser#dquote.
    def exitDquote(self, ctx:QueryParser.DquoteContext):
        pass


    # Enter a parse tree produced by QueryParser#us_sgn.
    def enterUs_sgn(self, ctx:QueryParser.Us_sgnContext):
        pass

    # Exit a parse tree produced by QueryParser#us_sgn.
    def exitUs_sgn(self, ctx:QueryParser.Us_sgnContext):
        pass


    # Enter a parse tree produced by QueryParser#c_and.
    def enterC_and(self, ctx:QueryParser.C_andContext):
        pass

    # Exit a parse tree produced by QueryParser#c_and.
    def exitC_and(self, ctx:QueryParser.C_andContext):
        pass


    # Enter a parse tree produced by QueryParser#c_and_hex.
    def enterC_and_hex(self, ctx:QueryParser.C_and_hexContext):
        pass

    # Exit a parse tree produced by QueryParser#c_and_hex.
    def exitC_and_hex(self, ctx:QueryParser.C_and_hexContext):
        pass


    # Enter a parse tree produced by QueryParser#c_or.
    def enterC_or(self, ctx:QueryParser.C_orContext):
        pass

    # Exit a parse tree produced by QueryParser#c_or.
    def exitC_or(self, ctx:QueryParser.C_orContext):
        pass


    # Enter a parse tree produced by QueryParser#c_slash.
    def enterC_slash(self, ctx:QueryParser.C_slashContext):
        pass

    # Exit a parse tree produced by QueryParser#c_slash.
    def exitC_slash(self, ctx:QueryParser.C_slashContext):
        pass


    # Enter a parse tree produced by QueryParser#c_dot.
    def enterC_dot(self, ctx:QueryParser.C_dotContext):
        pass

    # Exit a parse tree produced by QueryParser#c_dot.
    def exitC_dot(self, ctx:QueryParser.C_dotContext):
        pass


    # Enter a parse tree produced by QueryParser#c_colon.
    def enterC_colon(self, ctx:QueryParser.C_colonContext):
        pass

    # Exit a parse tree produced by QueryParser#c_colon.
    def exitC_colon(self, ctx:QueryParser.C_colonContext):
        pass


    # Enter a parse tree produced by QueryParser#s_bslash.
    def enterS_bslash(self, ctx:QueryParser.S_bslashContext):
        pass

    # Exit a parse tree produced by QueryParser#s_bslash.
    def exitS_bslash(self, ctx:QueryParser.S_bslashContext):
        pass


    # Enter a parse tree produced by QueryParser#c_q.
    def enterC_q(self, ctx:QueryParser.C_qContext):
        pass

    # Exit a parse tree produced by QueryParser#c_q.
    def exitC_q(self, ctx:QueryParser.C_qContext):
        pass


    # Enter a parse tree produced by QueryParser#par_open.
    def enterPar_open(self, ctx:QueryParser.Par_openContext):
        pass

    # Exit a parse tree produced by QueryParser#par_open.
    def exitPar_open(self, ctx:QueryParser.Par_openContext):
        pass


    # Enter a parse tree produced by QueryParser#par_close.
    def enterPar_close(self, ctx:QueryParser.Par_closeContext):
        pass

    # Exit a parse tree produced by QueryParser#par_close.
    def exitPar_close(self, ctx:QueryParser.Par_closeContext):
        pass


    # Enter a parse tree produced by QueryParser#c_star.
    def enterC_star(self, ctx:QueryParser.C_starContext):
        pass

    # Exit a parse tree produced by QueryParser#c_star.
    def exitC_star(self, ctx:QueryParser.C_starContext):
        pass


    # Enter a parse tree produced by QueryParser#c_percent.
    def enterC_percent(self, ctx:QueryParser.C_percentContext):
        pass

    # Exit a parse tree produced by QueryParser#c_percent.
    def exitC_percent(self, ctx:QueryParser.C_percentContext):
        pass


    # Enter a parse tree produced by QueryParser#c_brack.
    def enterC_brack(self, ctx:QueryParser.C_brackContext):
        pass

    # Exit a parse tree produced by QueryParser#c_brack.
    def exitC_brack(self, ctx:QueryParser.C_brackContext):
        pass


    # Enter a parse tree produced by QueryParser#c_acolad.
    def enterC_acolad(self, ctx:QueryParser.C_acoladContext):
        pass

    # Exit a parse tree produced by QueryParser#c_acolad.
    def exitC_acolad(self, ctx:QueryParser.C_acoladContext):
        pass


    # Enter a parse tree produced by QueryParser#c_dollar.
    def enterC_dollar(self, ctx:QueryParser.C_dollarContext):
        pass

    # Exit a parse tree produced by QueryParser#c_dollar.
    def exitC_dollar(self, ctx:QueryParser.C_dollarContext):
        pass


    # Enter a parse tree produced by QueryParser#c_adsgn.
    def enterC_adsgn(self, ctx:QueryParser.C_adsgnContext):
        pass

    # Exit a parse tree produced by QueryParser#c_adsgn.
    def exitC_adsgn(self, ctx:QueryParser.C_adsgnContext):
        pass


    # Enter a parse tree produced by QueryParser#c_irg1.
    def enterC_irg1(self, ctx:QueryParser.C_irg1Context):
        pass

    # Exit a parse tree produced by QueryParser#c_irg1.
    def exitC_irg1(self, ctx:QueryParser.C_irg1Context):
        pass



del QueryParser