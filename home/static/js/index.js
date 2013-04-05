(function(){
    soundManager.setup({
        url: window.STATIC_URL + 'vendor/soundmanager2/swf/',
        flashVersion: 9,
        useHTML5Audio: true,
        preferFlash: false,
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
                    textShow(song.artist + ' - ' + song.title);
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
                textShow(song.artist + ' - ' + song.title);
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
   var centerMap = null;
    google.maps.event.addDomListener(window, 'load', function() {
        var map = new google.maps.Map(document.getElementById('map'), {
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
                    "elementType": "labels.text.fill",
                    "stylers": [
                        { "color": "#67c7c0" }
                    ]
                },{
                    "elementType": "labels.text.stroke",
                    "stylers": [
                        { "color": "#ffffff" }
                    ]
                },
                {
                    "featureType": "water",
                    "elementType": "geometry.fill",
                    "stylers": [
                        { "color": "#c0c0c0" }
                    ]
                },{
                    "featureType": "poi",
                    "stylers": [
                        { "visibility": "off" }
                    ]
                },{
                    "featureType": "landscape.natural.terrain",
                    "stylers": [
                        { "visibility": "off" }
                    ]
                },{
                    "featureType": "landscape.natural.landcover",
                    "stylers": [
                        { "color": "#e0e0e0" }
                    ]
                },{
                    "featureType": "transit",
                    "stylers": [
                        { "visibility": "off" }
                    ]
                },{
                    "featureType": "road",
                    "elementType": "geometry.fill",
                    "stylers": [
                        { "color": "#a0a0a0" }
                    ]
                },{
                    "featureType": "road",
                    "elementType": "geometry.stroke",
                    "stylers": [
                        { "visibility": "off" }
                    ]
                },{
                    "featureType": "road.local",
                    "elementType": "geometry.fill",
                    "stylers": [
                        { "color": "#c0c0c0" }
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
                icon: new google.maps.MarkerImage(location.icon, null, null, new google.maps.Point(20, 40)),
                title: location.title,
                visible: true,
                zIndex: i
            });
            bounds.extend(position);

            var myOptions = {
                content: $('<div>').append($('<div>').addClass(location.css).html(location.content)).html(),
                disableAutoPan: false,
                maxWidth: 0,
                pixelOffset: new google.maps.Size(-130, -40),
                zIndex: null,
                infoBoxClearance: new google.maps.Size(1, 1),
                isHidden: false,
                pane: 'floatPane',
                enableEventPropagation: false,
                alignBottom: true
            };

            google.maps.event.addListener(marker, 'click', function (e) {
                ib.open(map, this);
            });
            var ib = new InfoBox(myOptions);

        });
        centerMap = function() {
            google.maps.event.trigger(map, "resize");
            map.fitBounds(bounds);
            map.setCenter(bounds.getCenter());
        };
        centerMap();
    });

    $('.to-map').click(function(){
        $('.rsvp, .card').fadeOut(200);
        $('.map').fadeIn(400);
        if (centerMap) {
            centerMap();
        }
    });

    $('.to-rsvp').click(function(){
        $('.map, .card').fadeOut(200);
        $('.rsvp').fadeIn(400);
    });

    $('.to-home').click(function(){
        $('.rsvp, .map, .card').fadeOut(200);
    });

    var toast = function(text) {
        var t = $('<div>');
        t.addClass('toast').text(text).appendTo($('body')).css({
            visibility: 'hidden',
            display: 'block'
        });
        setTimeout(function(){
            t.css({
                display: 'none',
                visibility: 'visible',
                zIndex: 100000,
                marginLeft: '-' + (t.width() / 2) + 'px',
                marginLTop: '-' + (t.height() / 2) + 'px'
            })
            .fadeIn(400, function(){
                setTimeout(function(){
                    t.fadeOut(200);
                }, 1000);
            });
        }, 1);
    };

    $('#rsvp').on('click', '.confirm span.attendance', function(e){
        e = $(e.target);
        e.toggleClass('active');
        confirmData({
            guests: [{id: e.parent().data('id'), 'attendance': e.hasClass('active')}]
        });
    });

    $('#rsvp').on('click', '.confirm span.celiac', function(e){
        e = $(e.target);
        e.toggleClass('active');
        confirmData({
            guests: [{id: e.parent().data('id'), 'celiac': e.hasClass('active')}]
        });
    });

    var messageTimeout;
    $('#rsvp').on('input', '.confirm textarea', function(e){
        clearTimeout(messageTimeout);
        messageTimeout = setTimeout(function(){
            confirmData({
                message: $('.rsvp .confirm textarea').val()
            });
        }, 500);
    });

    var confirmData = function(data){
        $.ajax({
            "type" : 'POST',
            "url" : '/confirm',
            "dataType" : 'json',
            'data' : {'post': JSON.stringify(data)},
            'success' : function (data) {
                if (!data.confirmed) {
                    toast('Algo se rompio... Intenta cargar la pagina nuevamente.');
                    $('#rsvp').html(data.html);
                }
            },
            'error' : function (data) {
                toast('Algo se rompio... Intenta cargar la pagina nuevamente.');
            }
        });
    };

    var confirmAll = function(){
        var data = {
            message: $('.rsvp .confirm textarea').val(),
            guests: []
        };
        $('#rsvp .confirm ul li').each(function(i, e){
            e = $(e);
            data.guests.push({
                id: e.data('id'),
                attendance: e.find('span.attendance').hasClass('active'),
                celiac: e.find('span.celiac').hasClass('active')
            });
        });
        $.ajax({
            "type" : 'POST',
            "url" : '/confirm',
            "dataType" : 'json',
            'data' : {'post': JSON.stringify(data)},
            'success' : function (data) {
                if (data.confirmed) {
                    $('.rsvp').fadeOut(200);
                    toast('Gracias por confirmar!');
                } else {
                    toast('Algo se rompio... Intenta cargar la pagina de nuevamente.');
                    $('#rsvp').html(data.html);
                }
            },
            'error' : function (data) {
                toast('Algo se rompio... Intenta cargar la pagina de nuevamente.');
            }
        });
    };

    var checkCode = function(){
        var data = {'code': $('#rsvp .code input[type=text]').val() };
        $.ajax({
            "type" : 'POST',
            "url" : '/code',
            "dataType" : 'json',
            'data' : {'post': JSON.stringify(data)},
            'success' : function (data) {
                if (data.invalid) {
                    toast('Codigo invalido.');
                } else {
                    $('#rsvp').html(data.html);
                }
            },
            'error' : function (data) {
                toast('Algo se rompio... Intenta cargar la pagina de nuevamente.');
            }
        });
    };

    $('#rsvp').on('click', '.confirm .footer input', confirmAll);
    $('#rsvp').on('click', '.code input[type=button]', checkCode)
    $('#rsvp').on('keypress', '.code input[type=text]', function(e){
       if (e.which == 13) {
           checkCode();
       }
    });

})();