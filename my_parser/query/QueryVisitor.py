# Generated from Query.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .QueryParser import QueryParser
else:
    from QueryParser import QueryParser

# This class defines a complete generic visitor for a parse tree produced by QueryParser.

class QueryVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by QueryParser#query.
    def visitQuery(self, ctx:QueryParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#p_id.
    def visitP_id(self, ctx:QueryParser.P_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#q_value.
    def visitQ_value(self, ctx:QueryParser.Q_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#value.
    def visitValue(self, ctx:QueryParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#ilg.
    def visitIlg(self, ctx:QueryParser.IlgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#label.
    def visitLabel(self, ctx:QueryParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#delim.
    def visitDelim(self, ctx:QueryParser.DelimContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#ch_ilg.
    def visitCh_ilg(self, ctx:QueryParser.Ch_ilgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#ldse.
    def visitLdse(self, ctx:QueryParser.LdseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#opNot.
    def visitOpNot(self, ctx:QueryParser.OpNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#opBinInvert.
    def visitOpBinInvert(self, ctx:QueryParser.OpBinInvertContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#opEqual.
    def visitOpEqual(self, ctx:QueryParser.OpEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#opLt.
    def visitOpLt(self, ctx:QueryParser.OpLtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#opGt.
    def visitOpGt(self, ctx:QueryParser.OpGtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#opMinus.
    def visitOpMinus(self, ctx:QueryParser.OpMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#opSem.
    def visitOpSem(self, ctx:QueryParser.OpSemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#cmt.
    def visitCmt(self, ctx:QueryParser.CmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#ddash.
    def visitDdash(self, ctx:QueryParser.DdashContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#quote.
    def visitQuote(self, ctx:QueryParser.QuoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#dquote.
    def visitDquote(self, ctx:QueryParser.DquoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#us_sgn.
    def visitUs_sgn(self, ctx:QueryParser.Us_sgnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#c_and.
    def visitC_and(self, ctx:QueryParser.C_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#c_and_hex.
    def visitC_and_hex(self, ctx:QueryParser.C_and_hexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#c_or.
    def visitC_or(self, ctx:QueryParser.C_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#c_slash.
    def visitC_slash(self, ctx:QueryParser.C_slashContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#c_dot.
    def visitC_dot(self, ctx:QueryParser.C_dotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#c_colon.
    def visitC_colon(self, ctx:QueryParser.C_colonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#s_bslash.
    def visitS_bslash(self, ctx:QueryParser.S_bslashContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#c_q.
    def visitC_q(self, ctx:QueryParser.C_qContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#par_open.
    def visitPar_open(self, ctx:QueryParser.Par_openContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#par_close.
    def visitPar_close(self, ctx:QueryParser.Par_closeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#c_star.
    def visitC_star(self, ctx:QueryParser.C_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#c_percent.
    def visitC_percent(self, ctx:QueryParser.C_percentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#c_brack.
    def visitC_brack(self, ctx:QueryParser.C_brackContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#c_acolad.
    def visitC_acolad(self, ctx:QueryParser.C_acoladContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#c_dollar.
    def visitC_dollar(self, ctx:QueryParser.C_dollarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#c_adsgn.
    def visitC_adsgn(self, ctx:QueryParser.C_adsgnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#c_irg1.
    def visitC_irg1(self, ctx:QueryParser.C_irg1Context):
        return self.visitChildren(ctx)



del QueryParser