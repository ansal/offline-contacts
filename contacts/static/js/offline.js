// Offline Module for the app

// Global backbone app
var App = App || {};

(function(){
    'use strict';

    App.offline = {};

    window.onoffline = function() {
        $('#offline_mode').show('fast');
        setTimeout(function(){
            $('#offline_mode').hide('fast');
        }, 8000);
    };

    window.ononline = function() {
        App.offline.sync();
        $('#online_mode').show('fast');
        setTimeout(function(){
            $('#online_mode').hide('fast');
        }, 8000);
    };

    function dumpLocalStorage(name) {
        var items = localStorage.getItem(name),
            data = [];

        if(!items) {
            return data;
        }

        items = items.split(',');
        for(var i = 0; i < items.length; i+= 1) {
            var item = JSON.parse(
                localStorage.getItem( App.LOCAL_STORAGE_NAME + '-' + items[i] )
            );
            data.push(item);
        }

        return data;

    }

    App.offline.sync = function() {
        if(!navigator.onLine) {
            return;
        }

        console.log('Syncing to server');
        
        var data = dumpLocalStorage(App.LOCAL_STORAGE_NAME);
        $.ajax({
            url: '/names/api/sync/',
            type: 'POST',
            dataType: 'json',
            data: {
                data: JSON.stringify( data )
            },
            success: function(data) {
                $('#sync_success').show('fast');
                setTimeout(function(){
                    $('#sync_success').hide('fast');
                }, 8000);
            },
            error: function(e) {
                $('#sync_error').show('fast');
                setTimeout(function(){
                    $('#sync_error').hide('fast');
                }, 8000);
                console.log('Error: ', e);
            }
        });
    };

    App.offline.fetch = function() {
        if(!navigator.onLine) {
            return;
        }

        $.getJSON('/names/api/contact/').success(function(names){
            _.each(names, function(name){
                App.contacts.create(name);
            });
        }).error(function(e){
            console.log('Error', e);
        });
    };

})();