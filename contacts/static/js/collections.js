// Collections for Offline Contact app

// Global backbone app
var App = App || {};

(function(){
  'use strict';

  App.LOCAL_STORAGE_NAME = 'offline-contacts';

  var ContactCollection = Backbone.Collection.extend({
    model: App.ContactModel,
    localStorage: new Backbone.LocalStorage(App.LOCAL_STORAGE_NAME),
  });

  App.contacts = new ContactCollection;

})();