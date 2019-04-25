odoo.define('customize_user_menu', function (require) {
    "use strict";

    var UserMenu = require('web.UserMenu');

    UserMenu.include({
        init: function () {
            this._super.apply(this, arguments);
            var self = this;

            self._rpc({
                model: 'ir.config_parameter',
                method: 'search_read',
                domain: [['key', '=like', 'hhplugins.hh_implement_%']],
                fields: ['key', 'value'],
                // lazy: false,
            }).then(function (res) {
                $.each(res, function (key, val) {
                    var dropdown_menu_item = self.$el.find('.dropdown-menu')[0].children;
                    $.each(dropdown_menu_item, function(i){
                        if (dropdown_menu_item[i].children[0]){
                            var menuItem = dropdown_menu_item[i].children[0].getAttribute('data-menu');
                            var configKey = val['key'].split('.')[1].split('_').pop();
                            if (configKey && menuItem && configKey == menuItem){
                                dropdown_menu_item[i].className = 'o_hidden';
                                if (configKey == 'shortcuts'){
                                    dropdown_menu_item[i+1].className = 'o_hidden';
                                }
                            }
                        }
                    });
                });
            })
        },

        start: function () {
            return this._super.apply(this, arguments);
        },
    });

});
