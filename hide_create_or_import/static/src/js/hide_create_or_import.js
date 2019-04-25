odoo.define('hide_create', function(require) {
    "use strict";

    var core = require('web.core');
    var qweb = core.qweb;
    // var KanbanController = require('web.KanbanController');
    var ListController = require('web.ListController');
    var ImportControllerMixin = {
        /**
         * @override
         */
        init: function (parent, model, renderer, params) {
            this.importEnabled = params.importEnabled;
        },

        //--------------------------------------------------------------------------
        // Private
        //--------------------------------------------------------------------------

        /**
         * Adds an event listener on the import button.
         *
         * @private
         */
        _bindImport: function () {
            if (!this.$buttons) {
                return;
            }
            var self = this;
            this.$buttons.on('click', '.o_button_import', function () {
                var state = self.model.get(self.handle, {raw: true});
                self.do_action({
                    type: 'ir.actions.client',
                    tag: 'import',
                    params: {
                        model: self.modelName,
                        context: state.getContext(),
                    }
                }, {
                    on_reverse_breadcrumb: self.reload.bind(self),
                });
            });
        }
    };
    var my_context;


     /**
     * Hide create or import button on list view
     * Eg. action item needed
     *
     * <field name="context">{'hide_create_btn':True}</field>
     * <field name="context">{'hide_import_btn':True}</field>
     **/
    ListController.include({
        init: function (parent, model, renderer, params) {
            this._super.apply(this, arguments);
            this.my_context = parent.dataset.context;
            ImportControllerMixin.init.apply(this, arguments);
        },

        renderButtons: function ($node) {
            if (!this.noLeaf && this.hasButtons) {
                this.$buttons = $(qweb.render('ListView.buttons', {widget: this}));
                this.$buttons.on('click', '.o_list_button_add', this._onCreateRecord.bind(this));
                this.$buttons.on('click', '.o_list_button_discard', this._onDiscard.bind(this));
                // check create button, if hide_create_btn is true, hide create and change color of import button
                if(this.my_context && this.my_context['hide_create_btn'] && this.my_context['hide_create_btn'] == true){
                    // suit for all module
                    if(this.$buttons.find('.o_list_button_add')[0].className && this.$buttons.find('.o_button_import')[0].className){
                        this.$buttons.find('.o_list_button_add')[0].className = 'btn btn-primary btn-sm o_list_button_add o_hidden';
                        this.$buttons.find('.o_button_import')[0].className = 'btn btn-sm btn-primary o_button_import';
                    }
                }
                // check import button
                if(this.my_context && this.my_context['hide_import_btn'] && this.my_context['hide_import_btn'] == true){
                    // suit for all module
                    if(this.$buttons.find('.o_button_import')[0].className){
                        this.$buttons.find('.o_button_import')[0].className = 'btn btn-sm btn-default o_button_import o_hidden';
                    }
                }
                this.$buttons.appendTo($node);
            }
            ImportControllerMixin._bindImport.call(this);
        },
    });

    // complete code below could allow hiding create button on kanban view
    // KanbanController.include({
    //     init: function () {
    //         this._super.apply(this, arguments);
    //         ImportControllerMixin.init.apply(this, arguments);
    //     },
    //
    //     //--------------------------------------------------------------------------
    //     // Public
    //     //--------------------------------------------------------------------------
    //
    //     /**
    //      * Extends the renderButtons function of ListView by adding an event listener
    //      * on the import button.
    //      *
    //      * @override
    //      */
    //     renderButtons: function () {
    //         this._super.apply(this, arguments); // Sets this.$buttons
    //         ImportControllerMixin._bindImport.call(this);
    //     }
    // });


});