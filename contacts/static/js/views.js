// Views for Offline Contact app

// Global backbone app
var App = App || {};

(function(){
  'use strict';

  var ENTER_KEY = 13;

  App.NameView = Backbone.View.extend({

    tagName: 'tr',
    events: {
        'click .edit_link': 'showEditor',
        'keyup .editor': 'dataChanged',
        'click .delete_button': 'deleteName'
    },
    template: _.template( $('#names_template').html() ),

    initialize: function() {
        this.listenTo(this.model, 'change', this.render);
        this.listenTo(this.model, 'destroy', this.remove);
    },

    render: function() {
      this.$el.html(this.template(this.model.toJSON()));
      return this;
    },

    showEditor: function(e) {
        e.preventDefault();
        var $info = this.$el.find('.info');
        $info.hide();
        var $editor = this.$el.find('.editor');
        $editor.show();
        this.$el.find('.editor_name').focus();
    },

    hideEditor: function() {
        this.$el.find('.editor_name').val( this.model.get('name') );
        this.$el.find('.editor_email').val( this.model.get('email') );
        this.$el.find('.editor_phone').val( this.model.get('phone') );
        var $info = this.$el.find('.info');
        $info.show();
        var $editor = this.$el.find('.editor');
        $editor.hide();
    },

    dataChanged: function(e) {
        e.preventDefault();
        if(e.which !== ENTER_KEY) {
            return;
        }

        var name = this.$el.find('.editor_name').val();
        var email = this.$el.find('.editor_email').val();
        var phone = this.$el.find('.editor_phone').val();
        if(!name || !email || !phone) {
            this.hideEditor();
            return;
        }
        this.model.set('name', name);
        this.model.set('email', email);
        this.model.set('phone', phone);
        this.model.save();
    },

    deleteName: function() {
        this.model.destroy();
    }

  });

  App.MainView = Backbone.View.extend({

    el: '#app',

    events: {
        'click #create_button': 'createName'
    },

    initialize: function() {
        this.$names = $('#names_list_body');
        this.$name = $('#name');
        this.$email = $('#email');
        this.$phone = $('#phone');
        this.$form_error = $('#form_error');
        this.listenTo(App.contacts, 'add', this.addOne);
        this.listenTo(App.contacts, 'reset', this.addAll);
    },

    addOne: function(name) {
      var view = new App.NameView({ model: name });
      this.$names.append(view.render().el);
    },

    addAll: function () {
      if( App.contacts.models.length === 0 ) {
        App.offline.fetch();
      } else {
        this.$names.html('');
        App.contacts.each(this.addOne, this);
      }
    },

    buildAttributes: function() {
        var attrs = {
            name: this.$name.val(),
            email: this.$email.val(),
            phone: this.$phone.val()
        };
        return attrs;
    },

    clearForm: function() {
        this.$name.val('');
        this.$email.val('');
        this.$phone.val('');
    },

    createName: function(e) {
        e.preventDefault();
        var attrs = this.buildAttributes();
        if( !attrs.name || !attrs.email || !attrs.phone) {
            this.$form_error.show();
            return;
        }

        App.contacts.create(attrs);
        this.$form_error.hide();
        this.clearForm();
        this.$name.focus();
    }

  });

})();