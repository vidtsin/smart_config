odoo.define('hide_popup_modal_footer', function (require) {
"use strict";

var ActionManager = require('web.ActionManager');
var Bus = require('web.Bus');

var Dialog = require('web.Dialog');
var dom = require('web.dom');

var ViewManager = require('web.ViewManager');

ActionManager.include({
    ir_actions_common: function(executor, options) {
        var self = this;
        if (executor.action.target === 'new') {
            var pre_dialog = (this.dialog && !this.dialog.isDestroyed()) ? this.dialog : null;
            if (pre_dialog){
                // prevent previous dialog to consider itself closed,
                // right now, as we're opening a new one (prevents
                // reload of original form view)
                pre_dialog.off('closed', null, pre_dialog.on_close);
            }
            if (this.dialog_widget && !this.dialog_widget.isDestroyed()) {
                this.dialog_widget.destroy();
            }
            // explicitly passing a closing action to dialog_stop() prevents
            // it from reloading the original form view
            this.dialog_stop(executor.action);
            this.dialog = new Dialog(this, _.defaults(options || {}, {
                title: executor.action.name,
                dialogClass: executor.klass,
                buttons: [],
                size: executor.action.context.dialog_size,
            }));

            // chain on_close triggers with previous dialog, if any
            this.dialog.on_close = function(){
                options.on_close.apply(null, arguments);
                if (pre_dialog && pre_dialog.on_close){
                    // no parameter passed to on_close as this will
                    // only be called when the last dialog is truly
                    // closing, and *should* trigger a reload of the
                    // underlying form view (see comments above)
                    pre_dialog.on_close();
                }
                if (!pre_dialog) {
                    self.dialog = null;
                }
            };
            this.dialog.on("closed", null, this.dialog.on_close);
            this.dialog_widget = executor.widget();
            var $dialogFooter;
            if (this.dialog_widget instanceof ViewManager) {
                executor.action.viewManager = this.dialog_widget;
                $dialogFooter = $('<div/>'); // fake dialog footer in which view
                                             // manager buttons will be put
                _.defaults(this.dialog_widget.flags, {
                    $buttons: $dialogFooter,
                    footer_to_buttons: true,
                });
                if (this.dialog_widget.action.view_mode === 'form') {
                    this.dialog_widget.flags.headless = true;
                }
            }
            if (this.dialog_widget.need_control_panel) {
                // Set a fake bus to Dialogs needing a ControlPanel as they should not
                // communicate with the main ControlPanel
                this.dialog_widget.set_cp_bus(new Bus());
            }
            this.dialog_widget.setParent(this.dialog);

            var fragment = document.createDocumentFragment();
            return this.dialog_widget.appendTo(fragment).then(function () {
                var def = $.Deferred();
                self.dialog.opened().then(function () {
                    dom.append(self.dialog.$el, fragment, {
                        in_DOM: true,
                        callbacks: [{widget: self.dialog_widget}],
                    });
                    if ($dialogFooter) {
                        // my code ********************************************************************
                        if(options.action.hide_footer != undefined && options.action.hide_footer){
                            // if(executor.action.context.access_right){
                            //     if(executor.action.context.access_right == true){
                            //         self.dialog.$footer.empty().append($dialogFooter.contents());
                            //     }
                            //     else{
                            self.dialog.$footer.empty();
                            //     }
                            // }
                        }
                        else{
                            self.dialog.$footer.empty().append($dialogFooter.contents());
                        }
                        // my code ********************************************************************
                    }
                    if (options.state && self.dialog_widget.do_load_state) {
                        return self.dialog_widget.do_load_state(options.state);
                    }
                })
                .done(def.resolve.bind(def))
                .fail(def.reject.bind(def));
                self.dialog.open();
                return def;
            }).then(function () {
                return executor.action;
            });
        }
        var def = this.inner_action && this.webclient && this.webclient.clear_uncommitted_changes() || $.when();
        return def.then(function() {
            self.dialog_stop(executor.action);
            return self.push_action(executor.action.viewManager = executor.widget(), executor.action, options).then(function () {
                return executor.action;
            });
        }).fail(function() {
            return $.Deferred().reject();
        });
    },
});
});