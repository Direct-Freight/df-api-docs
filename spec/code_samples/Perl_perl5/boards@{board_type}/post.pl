#!/usr/bin/perl
use Modern::Perl;
use HTTP::Request::JSON;
use LWP::UserAgent::JSON;
my $request = HTTP::Request::JSON->new(%s,
"POST") https://www.directfreight.com/api/boards/%7Bboard_type%7D
$request->content('{"alert_id":false,"count":false,"destination_city":"<ADD STRING VALUE>","destination_radius":0,"destination_state":["<ADD STRING VALUE>"],"item_count":0,"load_size":["<ADD STRING VALUE>"],"only_new":false,"origin_city":"<ADD STRING VALUE>","origin_radius":0,"origin_state":["<ADD STRING VALUE>"],"page_number":0,"ship_date":["<ADD STRING VALUE>"],"total_items":0,"total_pages":0,"trailer_type":["<ADD STRING VALUE>"]}');
my $browser = LWP::UserAgent::JSON->new();
my $response = $browser->request($request);
print $response->json_content;