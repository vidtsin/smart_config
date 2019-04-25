// odoo.define('record_highlighted.web', function (require) {
// "use strict";
//
//     var ListRenderer = require("web.ListRenderer");
// //    var ListController = require('web.ListController')
// //    var core = require('web.core');
// //    var _t = core._t;
//
//
//
//     ListRenderer.include({
//
//         _onRowClicked: function(event){
//             if(!window.getSelection().toString() && !event.ctrlKey){
//                 this._super.apply(this, arguments);
//             }
//         },
//         _onSelectRecord: function (event) {
//             this._super.apply(this, arguments);
//             this._rpc({
//                    model: 'res.config.settings',
//                    method: 'get_values',
//                    // args: ['shell_gas',],
//                    // domain: [
//                    //      ['name', '=', 'shell_gas']
//                    //  ],
//                    // context: self.odoo_context,
//                }).then(function(result) {
//                    if(result['record_highlighted']=='True'){
//                         var checkbox = $(event.currentTarget).find('input');
//                         var $selectedRow = $(checkbox).closest('tr')
//
//                         if($(checkbox).prop('checked')){
//                             $selectedRow.addClass('row_selected');
//                         } else {
//                             $selectedRow.removeClass('row_selected')
//                         }
//                    }
//             });
//
//         },
//         _onToggleSelection: function (event) {
//             this._super.apply(this, arguments);
//             this._rpc({
//                model: 'res.config.settings',
//                method: 'get_values',
//                // args: ['shell_gas',],
//                // domain: [
//                //      ['name', '=', 'shell_gas']
//                //  ],
//                // context: self.odoo_context,
//            }).then(function(result) {
//                if(result['record_highlighted']=='True') {
//                    var checked = $(event.currentTarget).prop('checked') || false;
//                    if (checked) {
//                        this.$('tbody .o_list_record_selector').closest('tr').addClass('row_selected')
//                    } else {
//                        this.$('tbody .o_list_record_selector').closest('tr').removeClass('row_selected')
//                    }
//                }
//            });
//         },
//     });
// });