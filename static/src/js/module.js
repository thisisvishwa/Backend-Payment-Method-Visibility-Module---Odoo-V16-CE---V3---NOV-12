odoo.define('payment_method_visibility.module', function (require) {
    "use strict";

    var core = require('web.core');
    var ListRenderer = require('web.ListRenderer');
    var ajax = require('web.ajax');

    var QWeb = core.qweb;
    var _t = core._t;

    ListRenderer.include({
        events: _.extend({}, ListRenderer.prototype.events, {
            'click .o_payment_method_info_button': '_onPaymentMethodInfoButton',
        }),

        _renderRow: function (record) {
            var self = this;
            var $row = this._super.apply(this, arguments);

            if (record.model === 'payment.method') {
                $row.addClass('o_payment_method_row');
                ajax.loadXML('/payment_method_visibility/static/src/xml/payment_method_button.xml', QWeb).then(function () {
                    var $button = $(QWeb.render('PaymentMethodButton', {widget: self}));
                    $row.find('.o_data_cell:last').after($button);
                });
            }
            return $row;
        },

        _onPaymentMethodInfoButton: function (event) {
            event.stopPropagation();
            var $target = $(event.currentTarget);
            var $row = $target.closest('.o_payment_method_row');
            var id = $row.data('id');

            this.do_action({
                type: 'ir.actions.act_window',
                res_model: 'payment.method',
                res_id: id,
                views: [[false, 'form']],
                target: 'current',
            });
        },
    });
});