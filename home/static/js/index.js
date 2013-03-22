soundManager.setup({
    url: '/static/vendor/soundmanager2/swf/',
    flashVersion: 9,
    useFlashBlock: false,
    debugFlash: false,
    debugMode: false,
    onready: function() {
        $.each(window.songs, function(i, song){
            soundManager.createSound({ id: song.id, url: song.url});
        });
        var current = 0; //Math.floor(Math.random() * window.songs.length);
        var textInterval;
        var textShow = function(text) {
            if (textInterval) {
                clearInterval(textInterval);
            }
            var ecurrent = $('.player .current');
            var end = 0;
            textInterval = setInterval(function(){
                if (end > text.length) {
                    clearInterval(textInterval);
                    textBlink(text);
                } else {
                    ecurrent.html(text.substring(0, end++).replace(/\s/g, '&nbsp;')).show();
                }
            }, 50);
        };
        var textBlink = function(text) {
            if (textInterval) {
                clearInterval(textInterval);
            }
            var ecurrent = $('.player .current');
            textInterval = setInterval(function(){
                clearInterval(textInterval);
                textHide(text);
            }, 2000);
        };
        var textHide = function(text) {
            if (textInterval) {
                clearInterval(textInterval);
            }
            var ecurrent = $('.player .current');
            var end = text.length;
            textInterval = setInterval(function(){
                if (end <= 0) {
                    clearInterval(textInterval);
                    ecurrent.hide();
                } else {
                    ecurrent.html(text.substring(0, end--).replace(/\s/g, '&nbsp;')).show();
                }
            }, 20);
        };
        var tooglePlay = function() {
            var song = window.songs[current];
            var sound = soundManager.getSoundById(song.id);
            if (sound.paused) {
                sound.play();
                textShow(song.artist + ' -' + song.title);
                $('.player .play').text('Pause');
            } else {
                sound.pause();
                $('.player .play').text('Play');
            }
        };
        var stop = function() {
            soundManager.stopAll();
        };
        var play = function(){
            var song = window.songs[current];
            soundManager.play(song.id, {volume: 100, onfinish: playNext});
            textShow(song.artist + ' -' + song.title);
        };
        var playNext = function() {
            current = current < window.songs.length - 1 ? current + 1 : 0;
            stop();
            play();
        };
        $('.player .next').click(playNext);
        $('.player .play').click(tooglePlay);
        play();
    }
});
google.maps.event.addDomListener(window, 'load', function() {
    var map = new google.maps.Map(document.getElementById("map"), {
        center: new google.maps.LatLng(-34.397, 150.644),
        zoom: 8,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        disableDefaultUI: true,
        zoomControl: true,
        zoomControlOptions: {
            style: google.maps.ZoomControlStyle.LARGE,
            position: google.maps.ControlPosition.RIGHT_TOP
        },
        styles: [
            {
                /*stylers: [
                    { hue: "#00ffe6" },
                    { saturation: -20 }
                ]*/
                stylers: [ { "gamma": 1.58 }, { "saturation": 30 }, { "weight": 0.1 } ]
            },{
                featureType: "road",
                elementType: "geometry",
                stylers: [
                    { lightness: 100 },
                    { visibility: "simplified" }
                ]
            }
        ]
    });
    var markers = [];
    var bounds = new google.maps.LatLngBounds();
    $.each(window.locations, function(i, location){
        var position = new google.maps.LatLng(location.latitude, location.longitude);
        var marker = new google.maps.Marker({
            position: position,
            map: map,
            /*icon: image,*/
            title: location.title,
            zIndex: i
        });
        bounds.extend(position);
    });
    map.fitBounds(bounds);
});

$('.to-map').click(function(){
    $('.map').animate({top: 0}, 1000);
});