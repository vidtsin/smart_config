odoo.define('dynamic_action_menu', function(require) {
    'use strict';

    /**
     * The action menu is rendered by the sidebar javascript. The 'renderer' object can contain a actionItem node if
     * we add it to ListRenderer. One is supposed to add a context field in action for menu in the xml and actionItems
     * should be a list.
     *
     * We can put the desired action items to the actionItems list in the context and the items will be available for
     * that specific page
     *
     * Eg. action item needed
     *
     * 'actionItems':{
                           'list': {
                                    'action':{'A': True},
                                    'other':{'Export':False, 'Delete':True}
                                   },
                           'form': {
                                    'action':{'B': False},
                                    'other':{'Duplicate':False, 'Delete':True}
                                   },
                          }
     * Otherwise, all the action menu items will be rendered
     **/

    let core = require('web.core');
    let FormRenderer = require('web.FormRenderer');
    let ListRenderer = require('web.ListRenderer');
    let Sidebar = require('web.Sidebar');
    var QWeb = core.qweb;


    var _t = core._t;  // This function is the Odoo builtin for translating strings. But it's weak af.

    FormRenderer.include({
        init: function (parent, state, params) {
                this._super.apply(this, arguments);

                try {
                    var actionMenu = parent["action"]["context"]["actionItems"]["form"];
                    if (actionMenu)
                        this.actionItems = actionMenu;
                }
                catch(err) {}
                // }
            }
        });

    ListRenderer.include({
            init: function (parent, state, params) {
                this._super.apply(this, arguments);

                try {
                    var actionMenu = parent["action"]["context"]["actionItems"]["list"];
                    if (actionMenu)
                        this.actionItems = actionMenu;
                }
                catch(err) {}
                // }
            }
        });

    Sidebar.include({
        _addToolbarActions: function (parent, toolbarActions) {
            var self = this;
            if (parent["renderer"]["actionItems"]) {
                _.each(['print', 'action', 'relate'], function (type) {
                    if (type in toolbarActions) {
                        var actionArray = [];
                        _.each(toolbarActions[type], function(actionItem) {
                            var customActions = parent["renderer"]["actionItems"]['action'];
                            if ((actionItem.sequence in customActions && customActions[actionItem.sequence])
                            || type === 'print') {
                                actionArray.push({
                                    "label": _t(actionItem.name),
                                    "action": actionItem
                                })
                            }
                        });
                        self._addItems(type === 'print' ? 'print' : 'other', actionArray);
                    }
                });


            var otherArray = [];  // put the matched item in and return the whole list for addItems()
            var customOther = parent['renderer']['actionItems']['other'];  // the dict for storing which items are required
            var transOther = {};  // to store the translated customOther dict keys when changing language

            for (var label in customOther) {  // This for loop is required to translate the dict keys
                var translatedLabel = _t(label);
                transOther[translatedLabel] = customOther[label];
            }


            for (var k = 0; k < toolbarActions.other.length; ++k) {
                var otherItems = toolbarActions.other[k];
                if (otherItems.label in transOther && transOther[otherItems.label] === true) {
                    otherArray.push(otherItems);
                }
            }
            self._addItems('other', otherArray);


            } else {
                this._super.apply(this, arguments);
            }
        },

        _redraw: function () {
            this.$el.html(QWeb.render('Sidebar', {widget: this}));
            var self = this;

            // Hides Sidebar sections when item list is empty
            this.$('.o_dropdown').each(function () {
                if (!$(this).find('li').length) {
                    $(this).hide();
                }
                /**
                 * Add line break between 'Action' menu items
                 * Eg. action item needed
                 *
                 * 'list': {
                            'action':{'0':True, '1':True, '2':True, '3':True, '4':True, '5':True, '6':True},
                            'other':{'Export':True, 'Delete':True},
                            'line_break':{'0':True, '1':True},
                            'delete_to_bottom':True,
                            'export_to_bottom':True,
                           },
                    'form': {
                            'action':{'0':True, '1':True, '2':True, '3':True, '4':True, '5':True, '6':True},
                            'other':{'Duplicate':False, 'Delete':False},
                            'line_break':{'1':True, '5':True},
                            'delete_to_bottom':True,
                            'duplicate_to_bottom':True,
                           },
                 * For list view, line break will be added to LIST after the first(0) item and the seventh(6) item
                 * For form view, line break will be added to LIST after the first(0) item and the seventh(6) item
                 * if **_to_botttom is true, it will be moved to the end of dropdown menu,
                   if both of export and delete is true, delete will be the last by default
                   if both of duplicate and delete is true, delete will be the last by default
                 * !!!! User must know the order of items on action menu
                 **/
                if(($(this).find('button')[0].innerHTML).includes('Action')){
                    if(self.env.context && self.env.context.actionItems){
                        var actItems = self.env.context.actionItems;
                        var baseURL = window.location.href.split('#')[1].split('&');

                        // get the view type for current interface == viewType
                        for(var item in baseURL){
                            if (baseURL[item].split('=')[0] == 'view_type'){
                                var viewType = baseURL[item].split('=')[1]
                            }
                        }
                        // re_order or add line_break for specific viewtype
                        for(var type in actItems){
                            if(type == viewType){
                                // add line_break
                                if (actItems[type].line_break){
                                    for (var line in actItems[type].line_break){
                                        if ($(this).find('li')[line]){
                                            $(this).find('li')[line].className += ' action_menu_line_break';
                                        }
                                    }
                                }
                            }
                        }

                    }
                }
            });

            this.$("[title]").tooltip({
                delay: { show: 500, hide: 0}
            });
            // this._super.apply(this, arguments);

        },
    })
});