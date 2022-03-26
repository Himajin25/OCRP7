
$(document).ready(function () {
    $("form").on('submit', function (event) {
        event.preventDefault();
        const url = 'http://127.0.0.1:5000/api';
        var ui = $('input:text').val()
        let display_question = function (ui) {
            return `<div class="message input"><p>${ui}</p></div>`

        }
        $('.messages').append(display_question(ui));
        $("form")[0].reset();
        $("input").prop('disabled', true);
        $('.loader').show();


        console.log(ui)

        $.ajax({
            url: url,
            data: { 'q': ui },
            dataType: 'json',
            success: function (data) {

                console.log(data);
                $("input").prop('disabled', false);
                $('.loader').hide();
                if (data.message == 'not found') {
                    $(".messages").append(unsuccesful(getRand(gp_fails)))
                } else {
                    const address = data.place_name
                    const bbox = data.bbox
                    const coord = data.center
                    const wiki = data.wiki
                    // const coord = data.items[0]['position']['lat'] +','+ data.items[0]['position']['lng']
                    const map_endpoint = 'https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/'
                    const map_marker = 'pin-s+555555(' + coord[0] + ',' + coord[1] + ')'
                    console.log(map_marker)
                    const map_coord = coord[0] + ',' + coord[1]
                    console.log(map_coord)
                    const map_zoom = ',' + '8'
                    const map_resolution = '600x200'
                    const map_url = map_endpoint + map_marker + '/' + map_coord + map_zoom + '/' + map_resolution + '?' + 'access_token=' + mapbox_token
                    console.log(map_url)
                    $(".messages").append(create_response(getRand(gp_thinking), getRand(gp_anectdote), address, map_url, wiki));
                }


            }
        })
    })
})

let unsuccesful = function (gp_fails) {
    return `<div class="message agent"><p>${gp_fails}</p></div>
            <div class="message agent"><p>Do you want to talk about some place else?</p></div>`

}

// let create_response = function(gp_greets, gp_anectdote, address, wiki, map_url){
let create_response = function (gp_thinking, gp_anectdote, address, map_url, wiki) {
    return `<div class="message agent"><p>${gp_thinking}</p></div>
    <div class="message agent"><p>if you mean "${address}", then I might even tell you more about it and show it to you on a map</p></div>
    <div class="message agent"><p>${gp_anectdote}</p></div>
    <div class="message agent"><p>You should know that ${wiki}</p></div>
    <div class="message agent"><p>Here is the map of  "${address}" :</p></div>
    <div class="message agent"><p><img id="map" src=${map_url}></p></div>
    <div class="message agent"><p>Do you want to talk about some place else?</p></div>`

}

let mapbox_token = 'pk.eyJ1IjoibmNiIiwiYSI6ImNrejN2NXFiNDA5NTMyb2sycGw0OWRyNWYifQ.HRSod30-jASUMraNtuxc-A'

gp_babble = {
    'gp_greets_and_aknowledges': ['hello, lemme think about it1', 'hello, lemme think about it2', 'hello, lemme think about it3'],
    'gp_greets_and_gives_address': ['hello, here is the address1', 'hello, here is the address2', 'hello, here is the address3'],
    'gp_adds_anectdote': ['this brings back memories, did you know that 1', 'this brings back memories, did you know that 2', 'this brings back memories, did you know that 3']
}


gp_thinking = ['hmmmmm... ah yes!']
gp_anectdote = ['this actually brings back memories... ']
gp_fails = ["I don't think i know about that place...or perharps i just don't remember 1", "I don't think i know about that place...or perharps i just don't remember 2", "I don't think i know about that place...or perharps i just don't remember 3", "I don't think i know about that place...or perharps i just don't remember 4", "I don't think i know about that place...or perharps i just don't remember 5"]

let getRand = function random_item(items) {

    return items[Math.floor(Math.random() * items.length)];

}


