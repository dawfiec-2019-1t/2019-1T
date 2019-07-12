var DATA;
var app;
var URL = "https://firebasestorage.googleapis.com/v0/b/governus-803f2.appspot.com/o/governus-803f2-export.json?alt=media&token=6962cc81-a7ea-41d5-a802-d35aea627880";

function load_data(){
    $.get(URL, function(data){
        DATA = data;
        app = new Vue({
            el: '#laws_app',
            data: {
                laws: DATA.law_data.laws,
                base_description: DATA.law_data.base_description
            }
        })
    });
}

load_data();
