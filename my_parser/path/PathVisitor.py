# Generated from Path.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PathParser import PathParser
else:
    from PathParser import PathParser

# This class defines a complete generic visitor for a parse tree produced by PathParser.

class PathVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PathParser#path.
    def visitPath(self, ctx:PathParser.PathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#p_value.
    def visitP_value(self, ctx:PathParser.P_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#value.
    def visitValue(self, ctx:PathParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#ilg.
    def visitIlg(self, ctx:PathParser.IlgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#label.
    def visitLabel(self, ctx:PathParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#delim.
    def visitDelim(self, ctx:PathParser.DelimContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#ch_ilg.
    def visitCh_ilg(self, ctx:PathParser.Ch_ilgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#ldse.
    def visitLdse(self, ctx:PathParser.LdseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#opNot.
    def visitOpNot(self, ctx:PathParser.OpNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#opBinInvert.
    def visitOpBinInvert(self, ctx:PathParser.OpBinInvertContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#opEqual.
    def visitOpEqual(self, ctx:PathParser.OpEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#opLt.
    def visitOpLt(self, ctx:PathParser.OpLtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#opGt.
    def visitOpGt(self, ctx:PathParser.OpGtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#opMinus.
    def visitOpMinus(self, ctx:PathParser.OpMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#opSem.
    def visitOpSem(self, ctx:PathParser.OpSemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#cmt.
    def visitCmt(self, ctx:PathParser.CmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#ddash.
    def visitDdash(self, ctx:PathParser.DdashContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#quote.
    def visitQuote(self, ctx:PathParser.QuoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#dquote.
    def visitDquote(self, ctx:PathParser.DquoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#us_sgn.
    def visitUs_sgn(self, ctx:PathParser.Us_sgnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#c_and.
    def visitC_and(self, ctx:PathParser.C_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#c_or.
    def visitC_or(self, ctx:PathParser.C_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#c_slash.
    def visitC_slash(self, ctx:PathParser.C_slashContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#c_slash_hex.
    def visitC_slash_hex(self, ctx:PathParser.C_slash_hexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#c_dot.
    def visitC_dot(self, ctx:PathParser.C_dotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#c_colon.
    def visitC_colon(self, ctx:PathParser.C_colonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#s_bslash.
    def visitS_bslash(self, ctx:PathParser.S_bslashContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#c_q.
    def visitC_q(self, ctx:PathParser.C_qContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#par_open.
    def visitPar_open(self, ctx:PathParser.Par_openContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#par_close.
    def visitPar_close(self, ctx:PathParser.Par_closeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#c_star.
    def visitC_star(self, ctx:PathParser.C_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#c_percent.
    def visitC_percent(self, ctx:PathParser.C_percentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#c_brack.
    def visitC_brack(self, ctx:PathParser.C_brackContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#c_acolad.
    def visitC_acolad(self, ctx:PathParser.C_acoladContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#c_dollar.
    def visitC_dollar(self, ctx:PathParser.C_dollarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#c_adsgn.
    def visitC_adsgn(self, ctx:PathParser.C_adsgnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathParser#c_irg1.
    def visitC_irg1(self, ctx:PathParser.C_irg1Context):
        return self.visitChildren(ctx)



del PathParser