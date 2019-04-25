odoo.define('switch_view', function (require) {
"use strict";

    /**
     * In the python script, write
     *
     * return {
     *    'type': 'ir.actions.act_view_reload', / ir_actions_go_back
     * }
     *
     */

    var ActionManager = require('web.ActionManager');

    ActionManager.include({
        ir_actions_act_view_reload: function (action, options) {
            window.location.reload();
        },

        ir_actions_go_back: function(action, options) {
            window.history.back();
        }
    });
});