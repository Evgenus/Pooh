from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1291324639.9260001
_template_filename='D:/Work/Research/__FUN__/POOH/pooh/source/pooh/2010/index.html'
_template_uri='/pooh/2010/index.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'template.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        PATH = context.get('PATH', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n<div>\n<h2>\u041f\u043e\u0441\u043b\u0435\u0441\u043b\u043e\u0432\u0438\u0435</h2>\n<p style="font-size: 12px">20.12.2009</p>\n<br />\n<p>\u0412\u0435\u0447\u0435\u0440 \u043f\u0440\u043e\u0448\u0435\u043b \u0445\u043e\u0440\u043e\u0448\u043e. \u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u043d\u043e\u0433\u043e \u043f\u043e \u043c\u0438\u043d\u0443\u0442\u0430\u043c \u043f\u043b\u0430\u043d\u0430 \u0434\u043b\u0438\u043d\u043e\u0439 \u0432 4.5 \u0447\u0430\u0441\u0430 \u0443\u0434\u0430\u043b\u043e\u0441\u044c \u043f\u0440\u0438\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0442\u044c\u0441\u044f \u0441 \u0442\u043e\u0447\u043d\u043e\u0441\u0442\u044c\u044e \u0434\u043e 5 \u043c\u0438\u043d\u0443\u0442. \u042f \u043e\u0447\u0435\u043d\u044c \u0440\u0430\u0434, \u043f\u0435\u0440\u0435\u043f\u043e\u043b\u043d\u0435\u043d, \u0438 \u0442\u0430\u043a\u043e\u0433\u043e \u0447\u0443\u0432\u0441\u0442\u0432\u0430 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0433\u043e \u0434\u043e\u043b\u0433\u0430, \u0441\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f, \u0434\u043e\u0441\u0442\u043e\u0439\u043d\u043e \u0440\u0435\u0430\u043b\u0438\u0437\u043e\u0432\u0430\u043d\u043d\u043e\u0439 \u0437\u0430\u0434\u0443\u043c\u043a\u0438 \u0443 \u043c\u0435\u043d\u044f \u0434\u0430\u0432\u043d\u043e \u043d\u0435 \u0431\u044b\u043b\u043e.\n</p>\n<h3>\u0411\u043b\u0430\u0433\u043e\u0434\u0430\u0440\u043d\u043e\u0441\u0442\u0438</h3>\n<p>\u041e\u0433\u0440\u043e\u043c\u043d\u043e\u0435 \u0441\u043f\u0430\u0441\u0438\u0431\u043e \u0443\u0447\u0430\u0441\u0442\u043d\u0438\u043a\u0430\u043c \u0438 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0442\u043e\u0440\u0430\u043c - \u0437\u0430 \u0432\u0441\u0451 \u0442\u043e, \u0447\u0442\u043e \u043c\u044b \u0441 \u0432\u0430\u043c\u0438 \u0441\u0443\u043c\u0435\u043b\u0438 \u0432\u043b\u043e\u0436\u0438\u0442\u044c, \u043f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u0438\u0442\u044c \u0438 \u0434\u043e\u043d\u0435\u0441\u0442\u0438, \u0437\u0430 \u0432\u0441\u0435 \u0440\u0435\u043f\u0435\u0442\u0438\u0446\u0438\u0438, \u0432\u044b\u0441\u043b\u0430\u043d\u043d\u044b\u0435 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044b, \u043f\u0440\u043e\u0434\u0443\u043c\u0430\u043d\u043d\u044b\u0435 \u0434\u0435\u0442\u0430\u043b\u0438, \u0437\u0430 \u044d\u0442\u0438 \u043d\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u044b\u0435 \u0436\u0438\u0437\u043d\u044c\u044e \u0434\u0432\u0430 \u043c\u0435\u0441\u044f\u0446\u0430; \u0434\u043e\u0431\u0440\u043e\u0432\u043e\u043b\u044c\u0446\u0430\u043c - \u0437\u0430 \u0441\u0442\u043e\u043b\u044c \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u0443\u044e \u043f\u043e\u043c\u043e\u0449\u044c \u0438 \u043f\u0443\u0431\u043b\u0438\u043a\u0435 - \u0437\u0430 \u0434\u0443\u0448\u0435\u0432\u043d\u044b\u0435 \u0442\u0435\u043f\u043b\u043e \u0438 \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0443, \u0441 \u043a\u043e\u0442\u043e\u0440\u044b\u043c\u0438 \u0432\u044b \u043f\u0440\u0438\u043d\u0438\u043c\u0430\u043b\u0438 \u043d\u0430\u0448\u0438 \u0432\u044b\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f, \u0437\u0430 \u043f\u043e\u043d\u0438\u043c\u0430\u043d\u0438\u0435, \u0441 \u043a\u043e\u0442\u043e\u0440\u044b\u043c \u043f\u0440\u043e\u0449\u0430\u043b\u0438 \u0442\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043e\u0433\u0440\u0435\u0445\u0438, \u0438 \u0437\u0430 \u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u044c \u0432 \u0431\u0440\u043e\u0441\u0430\u043d\u0438\u0438 \u0441\u0435\u0440\u0434\u0435\u0447\u0435\u043a \u0432 \u043c\u0435\u0448\u043e\u0447\u043a\u0438 :) </p>\n\n<h3>\u041f\u0440\u0438\u0433\u043b\u0430\u0448\u0435\u043d\u0438\u0435 \u043a \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u0447\u0435\u0441\u0442\u0432\u0443</h3>\n<p>\u042f \u0446\u0435\u043d\u044e \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u0447\u0435\u043b\u043e\u0432\u0435\u0447\u0435\u0441\u043a\u0438\u0445 \u043e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u0439 \u0438 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u0445\u0443\u0434\u043e\u0436\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430, \u043f\u0440\u0435\u0434\u043b\u0430\u0433\u0430\u0435\u043c\u043e\u0433\u043e \u043f\u0443\u0431\u043b\u0438\u043a\u0435, \u0438 \u0445\u043e\u0447\u0443 \u0434\u0432\u0438\u0433\u0430\u0442\u044c\u0441\u044f \u0432 \u044d\u0442\u043e\u043c \u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0438, \u043d\u0430\u0445\u043e\u0434\u044f\u0441\u044c \u0432 \u043f\u043e\u0441\u0442\u043e\u044f\u043d\u043d\u043e\u043c \u0438\u043d\u0442\u0435\u043d\u0441\u0438\u0432\u043d\u043e\u043c \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u0435 \u0441 \u043b\u044e\u0434\u044c\u043c\u0438, \u0446\u0435\u043b\u0438 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0441\u0445\u043e\u0436\u0438 \u0441 \u043c\u043e\u0438\u043c\u0438.\n\u0417\u0430\u0438\u043d\u0442\u0435\u0440\u0435\u0441\u043e\u0432\u0430\u043d \u0432 \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0435 \u0447\u0443\u0436\u043e\u0433\u043e \u0442\u0432\u043e\u0440\u0447\u0435\u0441\u0442\u0432\u0430 \u0438 \u0432 \u0441\u043e-\u0442\u0432\u043e\u0440\u0447\u0435\u0441\u0442\u0432\u0435. \u0415\u0441\u043b\u0438 \u0443 \u0432\u0430\u0441 \u0435\u0441\u0442\u044c \u0438\u0434\u0435\u0438 \u0441\u043e\u0432\u043c\u0435\u0441\u0442\u043d\u044b\u0445 \u043f\u0440\u043e\u0435\u043a\u0442\u043e\u0432/\u0432\u044b\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u0439, \u0435\u0441\u043b\u0438 \u044f \u043c\u043e\u0433\u0443 \u043a\u0430\u043a-\u0442\u043e \u0441\u043f\u043e\u0441\u043e\u0431\u0441\u0442\u0432\u043e\u0432\u0430\u0442\u044c \u0432\u0430\u0448\u0438\u043c \u043d\u0430\u0447\u0438\u043d\u0430\u043d\u0438\u044f\u043c, \u0435\u0441\u043b\u0438 \u0432\u0430\u043c \u0445\u043e\u0447\u0435\u0442\u0441\u044f \u0441\u043e \u043c\u043d\u043e\u0439 \u0447\u0435\u043c-\u0442\u043e \u043f\u043e\u0434\u0435\u043b\u0438\u0442\u044c\u0441\u044f, \u0438\u043b\u0438 \u0435\u0441\u043b\u0438 \u0432\u044b \u043f\u0440\u043e\u0441\u0442\u043e \u0447\u0443\u0432\u0441\u0442\u0432\u0443\u0435\u0442\u0435, \u0447\u0442\u043e \u043d\u0430\u0448\u0435 \u0441 \u0432\u0430\u043c\u0438 \u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u043e\u0431\u043e\u0433\u0430\u0442\u0438\u043b\u043e \u0431\u044b \u0438 \u0432\u0430\u0441, \u0438 \u043c\u0435\u043d\u044f - \u043f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430, \u043d\u0430\u043f\u0438\u0448\u0438\u0442\u0435, \u044f \u0431\u0443\u0434\u0443 \u043e\u0447\u0435\u043d\u044c \u0440\u0430\u0434.\n\u0425\u043e\u0447\u0443 \u0437\u0430\u043c\u0435\u0442\u0438\u0442\u044c, \u0447\u0442\u043e \u043c\u0435\u043d\u044f \u0438\u043d\u0442\u0435\u0440\u0435\u0441\u0443\u0435\u0442 \u0432 \u043f\u0435\u0440\u0432\u0443\u044e \u043e\u0447\u0435\u0440\u0435\u0434\u044c \u0441\u0443\u0442\u044c \u0432\u0430\u0448\u0435\u0433\u043e \u0442\u0432\u043e\u0440\u0447\u0435\u0441\u0442\u0432\u0430 \u0438 \u0432\u0430\u0448\u0435 \u0438\u043c \u0433\u043e\u0440\u0435\u043d\u0438\u0435, \u0430 \u043d\u0435 \u0432\u0430\u0448 \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b\u0438\u0437\u043c \u043d\u0430 \u0441\u0435\u0433\u043e\u0434\u043d\u044f\u0448\u043d\u0438\u0439 \u0434\u0435\u043d\u044c.</p>\n\n<h3>\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0430\u043c \u0438 \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u0430\u043c </h3>\n<p>\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0430\u043c: \u043f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430, \u043f\u043e \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u0438 \u043e\u043f\u0435\u0440\u0430\u0442\u0438\u0432\u043d\u043e \u0437\u0430\u043b\u0435\u0439\u0442\u0435 \u0432\u0430\u0448\u0438 \u0444\u043e\u0442\u043e \u043a\u0443\u0434\u0430-\u043d\u0438\u0431\u0443\u0434\u044c \u0438 \u043e\u0442\u043f\u0438\u0448\u0438\u0442\u0435\u0441\u044c.\n\u041e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u0430\u043c: \u044f \u043f\u043e\u043f\u0440\u043e\u0441\u0438\u043b \u0421\u0435\u0440\u0435\u0436\u0443 \u043f\u043e\u043c\u043e\u0447\u044c \u0441 \u043c\u043e\u043d\u0442\u0430\u0436\u0435\u043c, \u043f\u043e\u044d\u0442\u043e\u043c\u0443 \u0443\u0431\u0435\u0434\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u043f\u0440\u043e\u0448\u0443 \u043a\u0430\u043a \u043c\u043e\u0436\u043d\u043e \u0441\u043a\u043e\u0440\u0435\u0435 \u043f\u0435\u0440\u0435\u0434\u0430\u0442\u044c \u043c\u043d\u0435 \u043e\u0442\u0441\u043d\u044f\u0442\u044b\u0439 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b \u043d\u0430 \u0431\u043e\u043b\u0432\u0430\u043d\u043a\u0435(-\u043a\u0430\u0445), \u043c\u043e\u0436\u043d\u043e \u043f\u043e\u0436\u0430\u0442\u044b\u0439. </p>\n\n<h3>\u0423\u0447\u0430\u0441\u0442\u043d\u0438\u043a\u0430\u043c \u0438 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0442\u043e\u0440\u0430\u043c: \u0432\u0430\u0448\u0438 \u0434\u0430\u043d\u043d\u044b\u0435 \u043d\u0430 \u0441\u0430\u0439\u0442\u0435 </h3>\n<p>\u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e\u0442 \u0443\u0447\u0430\u0441\u0442\u043d\u0438\u043a\u043e\u0432: \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0441\u043b\u043e\u0432 \u043e \u0441\u0435\u0431\u0435 (\u0441\u043c. \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0435 \u043f\u0440\u0438\u043c\u0435\u0440\u044b \u043d\u0430 \u0441\u0430\u0439\u0442\u0435), \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u044b (\u043e\u043f\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e), \u0443\u0434\u0430\u0447\u043d\u043e\u0435 \u0444\u043e\u0442\u043e, \u043f\u043e\u0434\u043e\u0431\u043d\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u043e\u0432, \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0432 \u043d\u043e\u043c\u0435\u0440\u0435 (\u0430\u0432\u0442\u043e\u0440 \u043c\u0443\u0437\u044b\u043a\u0438, \u0430\u0432\u0442\u043e\u0440 \u0442\u0435\u043a\u0441\u0442\u0430 \u0438 \u0442.\u0434., \u043c\u043e\u0436\u043d\u043e \u0441\u043e \u0441\u0441\u044b\u043b\u043a\u0430\u043c\u0438 \u043d\u0430 \u0442\u0435\u043a\u0441\u0442\u044b/\u0430\u0443\u0434\u0438\u043e/\u0432\u0438\u0434\u0435\u043e).\n\u041e\u0442 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0442\u043e\u0440\u043e\u0432 \u0438 \u0434\u043e\u0431\u0440\u043e\u0432\u043e\u043b\u044c\u0446\u0435\u0432: \u0437\u0430 \u0447\u0442\u043e \u043e\u0442\u0432\u0435\u0447\u0430\u043b\u0438 \u043d\u0430 \u0432\u0435\u0447\u0435\u0440\u0435, \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u044b (\u043e\u043f\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e), \u0443\u0434\u0430\u0447\u043d\u043e\u0435 \u0444\u043e\u0442\u043e.\n\u0415\u0441\u043b\u0438 \u0434\u0430\u043d\u043d\u044b\u0435 \u043e \u0432\u0430\u0441 \u043d\u0435\u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u044b \u0438\u043b\u0438 \u043d\u0435 \u043f\u043e\u043b\u043d\u044b - \u043f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430, \u043d\u0430\u043f\u0438\u0448\u0438\u0442\u0435 \u043c\u043d\u0435 \u043e \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b\u0445 \u0438\u0437\u043c\u043d\u0435\u043d\u0438\u044f\u0445.\n\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 \u0443\u0447\u0430\u0441\u0442\u043d\u0438\u043a\u043e\u0432 \u0443\u0436\u0435 \u0435\u0441\u0442\u044c. \u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0442\u043e\u0440\u043e\u0432 \u0438 \u0434\u043e\u0431\u0440\u043e\u0432\u043e\u043b\u044c\u0446\u0435\u0432 \u0431\u0443\u0434\u0435\u0442 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0430 \u0432 \u0431\u043b\u0438\u0436\u0430\u0439\u0448\u0435\u0435 \u0432\u0440\u0435\u043c\u044f. </p>\n\n<h3>\u041e\u0442\u0437\u044b\u0432\u044b </h3>\n\n<p style="text-align: center;"><img src="')
        # SOURCE LINE 29
        __M_writer(unicode(PATH('/images/2010/pr2.jpg')))
        __M_writer(u'" class="pr" /></p>\n\n<p>\u042d\u0442\u043e\u0442 \u0432\u0435\u0447\u0435\u0440 \u043f\u0440\u0435\u0432\u0437\u043e\u0448\u0435\u043b \u0432\u0441\u0435 \u043c\u043e\u0438 \u0447\u0430\u044f\u043d\u0438\u044f \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u043e\u0442\u0437\u044b\u0432\u043e\u0432. \u042f \u043f\u043e\u043b\u0443\u0447\u0438\u043b \u0438\u043c\u0435\u043d\u043d\u043e \u0442\u043e, \u043e \u0447\u0435\u043c \u043c\u0435\u0447\u0442\u0430\u043b \u0443\u0436\u0435 \u0434\u0430\u0432\u043d\u043e - \u0441\u0432\u0435\u0442\u044f\u0449\u0438\u0435\u0441\u044f, \u0441\u0447\u0430\u0441\u0442\u043b\u0438\u0432\u044b\u0435 \u043b\u0438\u0446\u0430 \u043b\u044e\u0434\u0435\u0439, \u0438 \u0441\u043b\u043e\u0432\u0430 \u043d\u0435 \u043e \u0442\u043e\u043c, \u0447\u0442\u043e "\u041c\u0438\u0448\u0430 \u043a\u0440\u0443\u0442!"(\u0441), \u0430 \u0432 \u043f\u0435\u0440\u0432\u0443\u044e \u043e\u0447\u0435\u0440\u0435\u0434\u044c \u043e \u0442\u043e\u043c, \u0447\u0442\u043e \u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0443 \u0445\u043e\u0440\u043e\u0448\u043e \u0437\u0434\u0435\u0441\u044c, \u0447\u0442\u043e \u043e\u043d \u0432\u0434\u043e\u0445\u043d\u043e\u0432\u0438\u043b\u0441\u044f \u0431\u043b\u0430\u0433\u043e\u0434\u0430\u0440\u044f \u043c\u043d\u0435 \u0438 \u043c\u043e\u0438\u043c \u0434\u0440\u0443\u0437\u044c\u044f\u043c, \u0447\u0442\u043e \u043e\u043d \u0440\u0430\u0434, \u0447\u0442\u043e \u043f\u0440\u0438\u0448\u0435\u043b (\u0430 \u0437\u043d\u0430\u0447\u0438\u0442, \u0447\u0442\u043e \u043d\u0430\u0448\u0438 \u0443\u0441\u0438\u043b\u0438\u044f \u043e\u043f\u0440\u0430\u0432\u0434\u0430\u043b\u0438\u0441\u044c). \u0421\u043f\u0430\u0441\u0438\u0431\u043e \u0432\u0441\u0435\u043c, \u043c\u0438\u043c\u043e \u043a\u043e\u0433\u043e \u044f \u0443\u0441\u043f\u0435\u043b \u043f\u0440\u043e\u043c\u0435\u043b\u044c\u043a\u043d\u0443\u0442\u044c, \u0431\u0435\u0433\u0430\u044f \u043f\u043e \u0437\u0430\u043b\u0443 \u0432 \u0430\u043d\u0442\u0440\u0430\u043a\u0442\u0435 \u0438 \u043f\u043e\u0441\u043b\u0435 \u0437\u0430\u043a\u0440\u044b\u0442\u0438\u044f.\n\u041e\u0447\u0435\u043d\u044c \u0446\u0435\u043d\u043d\u044b \u0432\u0441\u0435 \u0432\u0438\u0434\u044b \u043e\u0442\u0437\u044b\u0432\u043e\u0432. \u0415\u0441\u043b\u0438 \u0432\u0430\u043c \u0435\u0441\u0442\u044c \u0447\u0442\u043e \u0441\u043a\u0430\u0437\u0430\u0442\u044c \u043c\u043d\u0435 \u0438\u043b\u0438 \u043a\u043e\u043c\u0443-\u0442\u043e \u0438\u0437 \u0443\u0447\u0430\u0441\u0442\u043d\u0438\u043a\u043e\u0432/\u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0442\u043e\u0440\u043e\u0432 - \u043f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430, \u043d\u0435 \u0441\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0439\u0442\u0435 \u0441\u0435\u0431\u044f :) </p>\n\n<h3>\u0412\u0430\u0448\u0430 \u0444\u0438\u043d\u0430\u043d\u0441\u043e\u0432\u0430\u044f \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0430 </h3>\n<p>\u041f\u0440\u043e\u0434\u0430\u0436\u0430 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043e\u043a \u043e\u043a\u0443\u043f\u0438\u043b\u0430 \u043f\u043e\u043b\u043e\u0432\u0438\u043d\u0443 \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u0438 \u0430\u0440\u0435\u043d\u0434\u044b \u0437\u0430\u043b\u0430. \u041e\u0442 \u0434\u0443\u0448\u0438 \u0431\u043b\u0430\u0433\u043e\u0434\u0430\u0440\u0438\u043c \u0432\u0441\u0435\u0445, \u043a\u0442\u043e \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u0430\u043b \u043d\u0430\u0441 \u0442\u0430\u0439\u043d\u043e \u0438\u043b\u0438 \u044f\u0432\u043d\u043e :) </p>\n\n<h3>\u0412\u044b\u0432\u043e\u0434\u044b</h3>\n<p>\u0434\u0435\u043b\u0430\u044e \u0432 \u0434\u0430\u043d\u043d\u044b\u0439 \u043c\u043e\u043c\u0435\u043d\u0442 \u0438 \u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u0442\u044c \u0438\u0445 \u0441\u0447\u0438\u0442\u0430\u044e \u043b\u0438\u0448\u043d\u0438\u043c. \u041f\u043e\u043b\u0443\u0447\u0430\u044e \u043e\u0442 \u0421\u0435\u0440\u0435\u0436\u0438 \u043c\u043d\u043e\u0433\u043e \u043a\u043e\u043d\u0441\u0442\u0440\u0443\u043a\u0442\u0438\u0432\u0430. \u0421\u0447\u0438\u0442\u0430\u044e, \u0447\u0442\u043e \u043f\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u043d\u044b\u0435 \u0437\u0430\u0434\u0430\u0447\u0438 \u0440\u0435\u0430\u043b\u0438\u0437\u043e\u0432\u0430\u043d\u044b \u0432 \u0434\u043e\u0441\u0442\u0430\u0442\u043e\u0447\u043d\u043e\u0439 \u0441\u0442\u0435\u043f\u0435\u043d\u0438. </p>\n\n<h3>\u041f\u043b\u0430\u043d\u044b \u043d\u0430 \u0431\u0443\u0434\u0443\u0449\u0435\u0435</h3>\n<p>\u041f\u043b\u0430\u043d\u043e\u0432 \u043e\u0447\u0435\u043d\u044c \u043c\u043d\u043e\u0433\u043e. \u0423\u0437\u043d\u0430\u0432\u0430\u0442\u044c \u043e \u043d\u0438\u0445 \u0432\u044b \u043c\u043e\u0436\u0435\u0442\u0435 \u0438\u0437 \u043c\u043e\u0435\u0433\u043e \u0416\u0416 \u0438 \u0447\u0430\u0441\u0442\u0438\u0447\u043d\u043e \u0438\u0437 \u044e\u0442\u0443\u0431-\u043a\u0430\u043d\u0430\u043b\u0430.\n\u041d\u0430\u0438\u0431\u043e\u043b\u044c\u0448\u0438\u0439 \u043f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442 \u0438\u043c\u0435\u0435\u0442 \u0441\u043e\u0432\u0435\u0440\u0448\u0435\u043d\u0441\u0442\u0432\u043e\u0432\u0430\u043d\u0438\u0435 \u043d\u0430\u0432\u044b\u043a\u043e\u0432 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f (\u0444\u043e\u0440\u0442\u0435\u043f\u0438\u0430\u043d\u043e, \u0432\u043e\u043a\u0430\u043b) \u0438 \u043a\u043e\u043c\u043f\u043e\u0437\u0438\u0442\u043e\u0440\u0430.\n\u0412 \u0431\u043b\u0438\u0436\u0430\u0439\u0448\u0438\u0435 \u043f\u043e\u043b\u0433\u043e\u0434\u0430 \u043d\u0430\u0434\u0435\u044e\u0441\u044c \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u043e\u0432\u0430\u0442\u044c \u0434\u0432\u0430 \u043a\u0430\u043c\u0435\u0440\u043d\u044b\u0445 \u043a\u043e\u043d\u0446\u0435\u0440\u0442\u0430. \u041f\u043e\u0434\u0440\u043e\u0431\u043d\u043e\u0441\u0442\u0438 - \u043f\u043e\u0442\u043e\u043c :)</p>\n\n<h3>\u041d\u0430 \u0437\u0430\u043a\u0443\u0441\u043a\u0443 </h3>\n<p>\u0412\u043e\u0442 \u0442\u0430\u043a\u043e\u0439 \u0432\u043e\u0442 \u0431\u044b\u043b \u0441\u0435\u043a\u0440\u0435\u0442\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440. \u041f\u0440\u043e\u0448\u0435\u043b \u043d\u0430 \u0443\u0440\u0430. \u0418\u0441\u043f\u044b\u0442\u0430\u043b \u043d\u0435\u043e\u043f\u0438\u0441\u0443\u0435\u043c\u043e\u0435 \u0443\u0434\u043e\u0432\u043e\u043b\u044c\u0441\u0442\u0432\u0438\u0435 \u043e\u0442 \u0440\u0435\u0430\u043a\u0446\u0438\u0438 \u0437\u0430\u043b\u0430 (\u043a\u0430\u043a \u0438 \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043b\u043e\u0441\u044c, \u0430\u043f\u043f\u043b\u043e\u0434\u0438\u0440\u043e\u0432\u0430\u043b\u0438 \u0441\u0442\u043e\u044f)</p>\n\n<p><object width="425" height="344"><param name="movie" value="http://www.youtube.com/v/fsXWbr71-EQ&hl=ru_RU&fs=1&"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed src="http://www.youtube.com/v/fsXWbr71-EQ&hl=ru_RU&fs=1&" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="425" height="344"></embed></object></p>\n\n\n<h2>\u041e \u0432\u0435\u0447\u0435\u0440\u0435!</h2>\n<p style="font-size: 12px">14.10.2009</p>\n<br />\n\n<p>\u0417\u0434\u0440\u0430\u0432\u0441\u0442\u0432\u0443\u0439\u0442\u0435.</p>\n\n<p>\u041c\u0435\u043d\u044f \u0437\u043e\u0432\u0443\u0442 \u041c\u0438\u0448\u0430 \u0420\u044b\u0431\u0430\u043a. \u041c\u043d\u0435 \u043f\u043e\u0441\u0447\u0430\u0441\u0442\u043b\u0438\u0432\u0438\u043b\u043e\u0441\u044c \u0438\u043c\u0435\u0442\u044c \u0434\u043e\u0441\u0442\u0430\u0442\u043e\u0447\u043d\u043e \u0431\u043e\u043b\u044c\u0448\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u043e\u044e\u0449\u0438\u0445, \u0442\u0430\u043d\u0446\u0443\u044e\u0449\u0438\u0445, \u0441\u043e\u0447\u0438\u043d\u044f\u044e\u0449\u0438\u0445 \u0438 \u043f\u0440\u043e\u0447\u0438\u0445 \u0434\u0440\u0443\u0437\u0435\u0439 \u0438 \u0437\u043d\u0430\u043a\u043e\u043c\u044b\u0445, \u0438 \u043e\u0447\u0435\u043d\u044c \u0445\u043e\u0447\u0435\u0442\u0441\u044f \u044d\u0442\u0438\u043c \u0434\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435\u043c \u043f\u043e\u0434\u0435\u043b\u0438\u0442\u044c\u0441\u044f \u0441 \u0432\u0430\u043c\u0438. :)</p>\n\n<p>\u041c\u044b \u0440\u0435\u0448\u0438\u043b\u0438 \u043f\u0440\u043e\u0432\u0435\u0441\u0442\u0438 \u043f\u0440\u0430\u0437\u0434\u043d\u0438\u0447\u043d\u043e\u0435 \u043f\u0440\u0435\u0434\u043d\u043e\u0432\u043e\u0433\u043e\u0434\u043d\u0435\u0435 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435, \u043f\u043e \u0444\u043e\u0440\u043c\u0430\u0442\u0443 \u0441\u0440\u0430\u0432\u043d\u0438\u043c\u043e\u0435 \u0441 \u043a\u0430\u043f\u0443\u0441\u0442\u043d\u0438\u043a\u043e\u043c.</p>\n\n<p>\u0421\u0443\u0442\u044c \u044d\u0442\u043e\u0433\u043e \u0432\u0435\u0447\u0435\u0440\u0430 \u0437\u0430\u043a\u043b\u044e\u0447\u0430\u0435\u0442\u0441\u044f \u0432 \u0442\u043e\u043c, \u0447\u0442\u043e\u0431\u044b \u043b\u044e\u0434\u0438 \u043f\u043e\u0434\u0435\u043b\u0438\u043b\u0438\u0441\u044c \u0434\u0440\u0443\u0433 \u0441 \u0434\u0440\u0443\u0433\u043e\u043c \u0441\u0432\u043e\u0438\u043c \u0442\u0432\u043e\u0440\u0447\u0435\u0441\u0442\u0432\u043e\u043c, \u0432\u0434\u043e\u0445\u043d\u043e\u0432\u0438\u043b\u0438 \u0434\u0440\u0443\u0433 \u0434\u0440\u0443\u0433\u0430, \u043f\u043e\u0437\u043d\u0430\u043a\u043e\u043c\u0438\u043b\u0438\u0441\u044c/\u043f\u043e\u0434\u0440\u0443\u0436\u0438\u043b\u0438\u0441\u044c \u0441 \u043d\u043e\u0432\u044b\u043c\u0438 \u0438\u043d\u0442\u0435\u0440\u0435\u0441\u043d\u044b\u043c\u0438 \u043b\u0438\u0447\u043d\u043e\u0441\u0442\u044f\u043c\u0438. \u041c\u044b \u043d\u0435 \u0441\u0442\u0430\u0432\u0438\u043b\u0438 \u0446\u0435\u043b\u0438 \u043f\u0440\u0438\u0433\u043b\u0430\u0448\u0430\u0442\u044c \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b\u043e\u0432, \u0432 \u043f\u0435\u0440\u0432\u0443\u044e \u043e\u0447\u0435\u0440\u0435\u0434\u044c \u044d\u0442\u043e \u0434\u0440\u0443\u0436\u0435\u0441\u043a\u0430\u044f \u0432\u0441\u0442\u0440\u0435\u0447\u0430, \u0433\u0434\u0435 \u0432\u0441\u0435 \u0432 \u0442\u043e\u0439 \u0438\u043b\u0438 \u0438\u043d\u043e\u0439 \u0441\u0442\u0435\u043f\u0435\u043d\u0438 \xab\u0441\u0432\u043e\u0438\xbb, \u0433\u0434\u0435 \u043a\u0430\u0436\u0434\u044b\u0439 \u0445\u043e\u0447\u0435\u0442 \u043f\u043e\u0440\u0430\u0434\u043e\u0432\u0430\u0442\u044c \u043e\u0441\u0442\u0430\u043b\u044c\u043d\u044b\u0445 \u0442\u0435\u043c, \u0447\u0435\u043c \u043c\u043e\u0436\u0435\u0442. \u041f\u0440\u0438 \u044d\u0442\u043e\u043c \u043c\u044b \u043e\u0447\u0435\u043d\u044c \u043f\u043e\u0441\u0442\u0430\u0440\u0430\u0435\u043c\u0441\u044f (\u0443\u0436\u0435 \u043e\u0447\u0435\u043d\u044c \u0441\u0442\u0430\u0440\u0430\u0435\u043c\u0441\u044f) \u0441\u0434\u0435\u043b\u0430\u0442\u044c \u044d\u0442\u043e \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u043e, \u0447\u0442\u043e\u0431\u044b \u0432\u0435\u0447\u0435\u0440 \u0438\u043c\u0435\u043b \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043d\u0443\u044e \u0445\u0443\u0434\u043e\u0436\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u0443\u044e \u0446\u0435\u043d\u043d\u043e\u0441\u0442\u044c. \u0414\u043e\u043b\u0436\u043d\u043e \u0431\u044b\u0442\u044c \u0438 \u0442\u0435\u043f\u043b\u043e, \u0438 \u043a\u0440\u0430\u0441\u0438\u0432\u043e. \u041e\u0431\u0435\u0449\u0430\u044e, \u0447\u0442\u043e \u0442\u0430\u043a \u0438 \u0431\u0443\u0434\u0435\u0442.</p>\n\n<p>\u041d\u0430\u0441 \u043f\u043e\u0440\u0430\u0434\u0443\u044e\u0442 \u0441\u0432\u043e\u0438\u043c\u0438 \u0432\u044b\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f\u043c\u0438 \u043a\u0430\u043a \u043a\u0438\u0435\u0432\u043b\u044f\u043d\u0435, \u0442\u0430\u043a \u0438 \u0433\u043e\u0441\u0442\u0438 \u0438\u0437 \u041a\u0440\u0430\u0441\u043d\u043e\u0434\u0430\u0440\u0430, \u041c\u0438\u043d\u0441\u043a\u0430, \u0421\u0430\u043d\u043a\u0442-\u041f\u0435\u0442\u0435\u0440\u0431\u0443\u0440\u0433\u0430, \u0415\u043a\u0430\u0442\u0435\u0440\u0438\u043d\u0431\u0443\u0440\u0433\u0430.</p>\n\n<p>\u0417\u0430 \u0445\u043e\u0434\u043e\u043c \u043f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u043a\u0438 \u043c\u043e\u0436\u043d\u043e \u0441\u043b\u0435\u0434\u0438\u0442\u044c \u0443 \u043c\u0435\u043d\u044f \u0432 \u0416\u0416: <a href="http://mrybak.livejournal.com/tag/%D0%BF%D1%83%D1%85+2010" class="green_a  ljicon">http://mrybak.livejournal.com</a></p>\n\n<p>\u0412\u0435\u0434\u0435\u0442\u0441\u044f \u0440\u0430\u0431\u043e\u0442\u0430 \u043d\u0430\u0434 \u0441\u0430\u0439\u0442\u043e\u043c, \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u043c\u044b \u043f\u043e\u0442\u043e\u043c (\u043c\u044b \u043d\u0430\u0434\u0435\u0435\u043c\u0441\u044f) \u0432\u044b\u043b\u043e\u0436\u0438\u043c \u0432\u0438\u0434\u0435\u043e \u0432\u0441\u0435\u0445 \u043d\u043e\u043c\u0435\u0440\u043e\u0432 \u0438 \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u044b \u0432\u0441\u0435\u0445 \u0443\u0447\u0430\u0441\u0442\u043d\u0438\u043a\u043e\u0432.</p>\n<p style=\'text-align: center;\'><img src="')
        # SOURCE LINE 68
        __M_writer(unicode(PATH('/images/2010/pooh2010_invite.jpg')))
        __M_writer(u'" /></p>\n<p>\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0434\u043b\u0438\u0442\u0441\u044f 3 \u0447\u0430\u0441\u0430 \u0438 \u0441\u043e\u0441\u0442\u043e\u0438\u0442 \u0438\u0437 \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0445 \u0431\u043b\u043e\u043a\u043e\u0432:</p>\n<ul class="contact_info" style="font-size: 14px">\n    <li></li>\n    <li>\xab\u041a\u043e\u0433\u0434\u0430 \u0411\u0430\u0445 \u0443\u043b\u044b\u0431\u0430\u0435\u0442\u0441\u044f\xbb (\u043c\u0443\u0437\u044b\u043a\u0430 \u0432 \u0441\u0442\u0438\u043b\u044f\u0445 \u0431\u0430\u0440\u043e\u043a\u043a\u043e, \u0434\u0436\u0430\u0437 \u0438 \u0431\u0430\u0440\u043e\u043a\u043a\u043e-\u0434\u0436\u0430\u0437)</li>\n    <li>\xab\u0423\u0433\u043e\u043b\u043e\u043a \u0438\u043d\u0442\u0438\u043c\u043d\u043e\u0439 \u043b\u0438\u0440\u0438\u043a\u0438\xbb (\u0440\u043e\u043c\u0430\u043d\u0441, \u0430\u0432\u0442\u043e\u0440\u0441\u043a\u0438\u0435 \u0441\u0442\u0438\u0445\u0438)</li>\n    <li>\xab\u041f\u0440\u043e\u0449\u0430\u043d\u0438\u0435 \u0441 \u043e\u0441\u0435\u043d\u044c\u044e\xbb (\u0434\u0435\u043a\u043b\u0430\u043c\u0430\u0446\u0438\u044f \u043f\u043e\u0434 \u043c\u0443\u0437\u044b\u043a\u0443)</li>\n    <li>\xab\u0422\u0443\u0434\u0443\u043c-\u0442\u044b\u0449\xbb (\u044e\u043c\u043e\u0440\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0431\u043b\u043e\u043a)</li>\n    <li>\xab\u0423\u0433\u043e\u043b\u043e\u043a \u0430\u0432\u0442\u043e\u0440\u0441\u043a\u043e\u0439 \u043f\u0435\u0441\u043d\u0438\xbb (\u0430\u0432\u0442\u043e\u0440\u0441\u043a\u0430\u044f \u043f\u0435\u0441\u043d\u044f!)</li>\n    <li>\xab\u0423\u0433\u043e\u043b\u043e\u043a \u043d\u0435\u0430\u0432\u0442\u043e\u0440\u0441\u043a\u043e\u0439 \u043f\u0435\u0441\u043d\u0438\xbb (\u043f\u0440\u043e\u0441\u0442\u043e \u043f\u0435\u0441\u043d\u044f)</li>\n    <li>\xab\u0423\u0433\u043e\u043b\u043e\u043a \u0442\u0435\u0430\u0442\u0440\u0430\xbb (\u043a\u043e\u0440\u043e\u0442\u043a\u0438\u0439 \u043c\u043e\u043d\u043e\u0441\u043f\u0435\u043a\u0442\u0430\u043a\u043b\u044c)</li>\n    <li>\xab\u0423\u0433\u043e\u043b\u043e\u043a \u041c\u0438\u0448\u0438 \u041e\u043a\u0443\u043d\u0435\u0432\u0430!\xbb (\u0444\u043e\u0440\u0442\u0435\u043f\u0438\u0430\u043d\u043d\u0430\u044f \u043c\u0443\u0437\u044b\u043a\u0430)</li>\n    <li>\xab\u0427\u0435\u043b\u043e\u0432\u0435\u043a \u0412\u043e\u0441\u043f\u0438\u0442\u0430\u043d\u043d\u044b\u0439\xbb (\u0441\u0442\u0438\u0445\u0438, \u0433\u0438\u0442\u0430\u0440\u043d\u0430\u044f/\u0444\u043e\u0440\u0442\u0435\u043f\u0438\u0430\u043d\u043d\u0430\u044f \u043c\u0443\u0437\u044b\u043a\u0430, \u043f\u0435\u0441\u043d\u0438; \u0441\u043e\u043b\u044c\u043d\u0430\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0430 \u0441 \u043d\u0438\u043a\u043e\u043c \u0412\u043e\u0441\u043f\u0438\u0442\u0430\u043d\u043d\u044b\u0439)</li>\n    <li>\xab\u0421\u0442\u0430\u0440\u0438\u043d\u043d\u044b\u0439 \u0442\u0430\u043d\u0435\u0446 \u0438 \u0441\u0442\u0430\u0440\u0438\u043d\u043d\u044b\u0439 \u0431\u0430\u0440\u0430\u0431\u0430\u043d\xbb (\u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u043e)</li>\n    <li>\xab\u0423\u0433\u043e\u043b\u043e\u043a \u043c\u044e\u0437\u0438\u043a\u043b\u043e\u0432 \u0438 \u0441\u0435\u0440\u0438\u0430\u043b\u043e\u0432\xbb (\u0444\u0430\u043d-\u0430\u0440\u0442)</li>\n    <li>\xab\u041d\u0435\u043c\u043d\u043e\u0436\u043a\u043e \u0441\u0432\u0438\u043d\u0433\u0430\xbb (\u043e\u0442 \u0421\u0430\u0448\u0438 \u041c\u0430\u0440\u0438\u043d\u0438\u0447\u0430, \u0441\u0438\u043b\u044c\u043d\u043e\u0433\u043e \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0435\u043b\u044f \u043a\u0438\u0435\u0432\u0441\u043a\u043e\u0439 \u0448\u043a\u043e\u043b\u044b)</li>\n</ul>\n<p>\u041e \u043d\u0435\u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0438\u0437 \u044d\u0442\u0438\u0445 \u0431\u043b\u043e\u043a\u043e\u0432 \u0432 \u0442\u0435\u0447\u0435\u043d\u0438\u0435 \u0431\u043b\u0438\u0436\u0430\u0439\u0448\u0438\u0445 \u0434\u0432\u0443\u0445 \u043d\u0435\u0434\u0435\u043b\u044c \u043f\u043e\u044f\u0432\u044f\u0442\u0441\u044f \u043f\u043e\u0441\u0442\u044b \u0443 \u043c\u0435\u043d\u044f \u0432 \u0416\u0416 \u043f\u043e \u0432\u044b\u0448\u0435\u0443\u043a\u0430\u0437\u0430\u043d\u043d\u043e\u0439 \u0441\u0441\u044b\u043b\u043a\u0435.</p>\n\n<p><a href="where.html" class=\'link\'>\u0412\u0440\u0435\u043c\u044f \u0438 \u043c\u0435\u0441\u0442\u043e \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f</a>:</p>\n\n<p>19 \u0434\u0435\u043a\u0430\u0431\u0440\u044f 2009 \u0433.,\n19:00-22:00,\n\u0411\u043e\u043b\u044c\u0448\u043e\u0439 \u043a\u043e\u043d\u0444\u0435\u0440\u0435\u043d\u0446-\u0437\u0430\u043b \u0413\u041a \xab\u0422\u0443\u0440\u0438\u0441\u0442\xbb\n(100 \u043c \u043e\u0442 \u043c. \xab\u041b\u0435\u0432\u043e\u0431\u0435\u0440\u0435\u0436\u043d\u0430\u044f\xbb, \u0443\u043b. \u0420. \u041e\u043a\u0438\u043f\u043d\u043e\u0439, 2).</p>\n\n<p>\u0412\u0445\u043e\u0434 \u0441\u0432\u043e\u0431\u043e\u0434\u043d\u044b\u0439. \u041c\u044b \u0431\u0443\u0434\u0435\u043c \u0440\u0430\u0434\u044b \u0432\u0430\u043c \u0438 \u0432\u0430\u0448\u0438\u043c \u0434\u0440\u0443\u0437\u044c\u044f\u043c, \u043c\u0435\u0441\u0442\u0430 \u0445\u0432\u0430\u0442\u0438\u0442 \u0432\u0441\u0435\u043c; \u043f\u0440\u0438\u0445\u043e\u0434\u0438\u0442\u0435! :)</p>\n\n<p>P.S. \u0412\u0410\u0416\u041d\u041e:</p>\n\n<p>\u0425\u043e\u0447\u0435\u0442\u0441\u044f \u0441\u0434\u0435\u043b\u0430\u0442\u044c \u043e\u0433\u043e\u0432\u043e\u0440\u043a\u0443. \u041c\u044b \u043f\u0440\u043e\u0442\u0438\u0432 \u043f\u0438\u0432\u0430, \u0442\u0443\u043f\u043e\u0433\u043e \u0440\u0436\u0430\u0447\u0430, \u0433\u043b\u0430\u043c\u0443\u0440\u043d\u044b\u0445 \u0431\u043b\u043e\u043d\u0434\u0438\u043d\u043e\u043a, \xab\u043f\u043e\u0432\u0438\u0441\u0435\u0442\u044c \u0432 \u043a\u043b\u0443\u0431\u0435\xbb \u0438 \u043f\u0440\u043e\u0447\u0435\u0433\u043e \u043d\u0435\u0430\u0434\u0435\u043a\u0432\u0430\u0442\u0430 \u0432 \u043e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u0438 \u044d\u0442\u043e\u0433\u043e \u0432\u0435\u0447\u0435\u0440\u0430. \u042d\u0442\u043e \u043a\u0443\u043b\u044c\u0442\u0443\u0440\u043d\u043e\u0435 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435, \u0432\u0445\u043e\u0434 \u0441 \u043f\u0438\u0432\u043e\u043c/\u043f\u043e\u043f\u043a\u043e\u0440\u043d\u043e\u043c \u0437\u0430\u043f\u0440\u0435\u0449\u0435\u043d, \u0438\u0434\u0438\u043e\u0442\u043e\u0432/\u0442\u0440\u043e\u043b\u043b\u0435\u0439 \u043c\u044b \u0431\u0443\u0434\u0435\u043c \u0432\u044b\u0441\u0442\u0430\u0432\u043b\u044f\u0442\u044c. \u042d\u0442\u0438 \u043e\u0447\u0435\u0432\u0438\u0434\u043d\u044b\u0435 \u0432\u0435\u0449\u0438 \u043b\u0443\u0447\u0448\u0435 \u0432\u0441\u0435-\u0442\u0430\u043a\u0438 \u043f\u0440\u043e\u0433\u043e\u0432\u043e\u0440\u0438\u0442\u044c. \u041f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430, \u0434\u0443\u043c\u0430\u0439\u0442\u0435, \u043a\u043e\u0433\u043e \u0432\u044b \u0437\u043e\u0432\u0435\u0442\u0435 \u0438\u0437 \u0434\u0440\u0443\u0437\u0435\u0439. \u0415\u0441\u043b\u0438 \u0443\u0432\u0435\u0440\u0435\u043d\u044b, \u0447\u0442\u043e \u044d\u0442\u043e \u043d\u0435 \u043f\u0440\u043e \u0412\u0430\u0441 - \u043e\u0447\u0435\u043d\u044c \u0445\u043e\u0440\u043e\u0448\u043e. \u0415\u0441\u043b\u0438 \u043d\u0435 \u0443\u0432\u0435\u0440\u0435\u043d\u044b - \u043b\u0443\u0447\u0448\u0435 \u043f\u043e\u0434\u0443\u043c\u0430\u0439\u0442\u0435 \u0434\u0432\u0430\u0436\u0434\u044b.</p>\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


