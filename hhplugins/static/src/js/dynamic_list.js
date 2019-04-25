// odoo.define('kt_dynamic_list.shcolumns', function (require) {
// "use strict";
//
// var core = require('web.core');
// var BaseImport = require('base_import.import');
// var ListController= require('web.ListController');
// var QWeb = core.qweb;
// var tag;
//
// ListController.include({
//    renderButtons: function($node) {
//        this._super.apply(this, arguments);
//        var myThis = this;
//        myThis.$buttons.find('.dynamic_dropdown_btn')[0].className='dynamic_dropdown_btn o_hidden btn-group hidden-xs o_dropdown';
//
//        console.log('before', new Date().getMilliseconds());
//        this._rpc({
//            model: 'res.config.settings',
//            method: 'get_values',
//            // args: ['shell_gas',],
//            // domain: [
//            //      ['name', '=', 'shell_gas']
//            //  ],
//            // context: self.odoo_context,
//        }).then(function(result) {
//            if(result['kt_dynamic_list'] == 'True'){
//                myThis.tag = true;
//            }
//            else{
//                myThis.tag = false;
//            }
//            console.log('after', new Date().getMilliseconds());
//        });
//
//
//        setTimeout(function() {
//            if(myThis.tag==true){
//                console.log(myThis.tag, 'true');
//                myThis.$buttons.find('.dynamic_dropdown_btn')[0].className='dynamic_dropdown_btn btn-group hidden-xs o_dropdown';
//                if (!myThis.noLeaf && myThis.hasButtons) {
//                     // myThis.$buttons = $(QWeb.render('dynamic_list_view_buttons', {widget: myThis}));
//                     // myThis.$buttons.on('click', '.o_list_button_add', myThis._onCreateRecord.bind(myThis));
//                     // myThis.$buttons.on('click', '.o_list_button_discard', myThis._onDiscard.bind(myThis));
//                     myThis.$buttons.on('click', '.oe_select_columns', myThis.my_setup_columns.bind(myThis));
//                     myThis.$buttons.on('click', '.oe_dropdown_btn', myThis.hide_show_columns.bind(myThis));
//                     myThis.$buttons.on('click', '.oe_dropdown_menu', myThis.stop_event.bind(myThis));
//                     // myThis.$buttons.appendTo($node);
//                }
//                 if (myThis.$buttons){
//                     myThis.contents = myThis.$buttons.find('ul#showcb');
//                     var columns = [];
//                     _.each(myThis.renderer.arch.children, function(node){
//                         var name = node.attrs.name;
//                         var description = node.attrs.string || myThis.renderer.state.fields[name].string;
//                         columns.push({
//                             'field_name': node.attrs.name,
//                             'label': description,
//                             'invisible': node.attrs.modifiers.column_invisible || false
//                         })
//                     });
//                     myThis.contents.append($(QWeb.render('ColumnSelectionDropDown',{widget:myThis,columns:columns})));
//                 }
//                 console.log($node);
//            }
//            else{
//                console.log(myThis.tag, 'false');
//
//                 // if (!myThis.noLeaf && myThis.hasButtons) {
//                 //     myThis.$buttons = $(QWeb.render('ListView.buttons', {widget: myThis}));
//                 //     myThis.$buttons.on('click', '.o_list_button_add', myThis._onCreateRecord.bind(myThis));
//                 //     myThis.$buttons.on('click', '.o_list_button_discard', myThis._onDiscard.bind(myThis));
//                 //     myThis.$buttons.appendTo($node);
//                 // }
//            }
//         }, 500);
//
//
//        // console.log('1', myThis);
//        // console.log('2', this);
//
//
//        //      if (!this.noLeaf && this.hasButtons) {
//        //          this.$buttons.on('click', '.oe_select_columns', this.my_setup_columns.bind(this));
//        //          this.$buttons.on('click', '.oe_dropdown_btn', this.hide_show_columns.bind(this));
//        //          this.$buttons.on('click', '.oe_dropdown_menu', this.stop_event.bind(this));
//        //      }
//        //      if (this.$buttons){
//        //          this.contents = this.$buttons.find('ul#showcb');
//        //          var columns = []
//        //          _.each(this.renderer.arch.children, function(node){
//        //              var name = node.attrs.name
//        //              var description = node.attrs.string || self.renderer.state.fields[name].string;
//        //              columns.push({
//        //                  'field_name': node.attrs.name,
//        //                  'label': description,
//        //                  'invisible': node.attrs.modifiers.column_invisible || false
//        //              })
//        //          })
//        //          this.contents.append($(QWeb.render('ColumnSelectionDropDown',{widget:this,columns:columns})));
//        //      }
//     },
//
//     my_setup_columns: function () {
//         $("#showcb").toggle();
//     },
//     stop_event : function(e)
//     {
//         e.stopPropagation();
//     },
//
//     hide_show_columns : function(){
//        $("#showcb").hide();
//        this.setup_columns();
//        var state = this.model.get(this.handle);
//        this.renderer.updateState(state, {reload: true})
//     },
//
//     setup_columns: function () {
//         var self = this;
//         _.each(this.contents.find('li.item_column'), function(item){
//             var checkbox_item = $(item).find('input');
//             var field = _.find(self.renderer.arch.children, function(field){
//                 return field.attrs.name === checkbox_item.data('name')
//             });
//             if(checkbox_item.prop('checked')){
//                 field.attrs.modifiers.column_invisible = false;
//             }
//             else {
//                 field.attrs.modifiers.column_invisible = true;
//             }
//         })
//     },
// });
//
//     $(document).click(function(){
//       $("#showcb").hide();
//     });
//
// });