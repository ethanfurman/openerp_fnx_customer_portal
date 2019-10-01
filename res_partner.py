import logging
from osv import osv
# from tools.misc import EnumNoAlias

_logger = logging.getLogger(__name__)


class res_partner(osv.Model):
    """
    Only show user's matching partner.
    """
    _name = 'res.partner'
    _inherit = 'res.partner'

    def search(self, cr, uid, args, offset=0, limit=None, order=None, context=None, count=False):
        if context is None:
            context = {}
        if context.get('fnx_customer_portal_account'):
            res_users = self.pool.get('res.users')
            user = res_users.browse(cr, uid, uid, context=context)
            if isinstance(args, list):
                args.append(('xml_id','=',user.fis_partner_code))
            elif isinstance(args, tuple):
                args = args + (('xml_id','=',user.fis_partner_code), )
        return super(res_partner, self).search(
                cr, uid, args,
                offset=offset,
                limit=limit,
                order=order,
                context=context,
                count=count,
                )
