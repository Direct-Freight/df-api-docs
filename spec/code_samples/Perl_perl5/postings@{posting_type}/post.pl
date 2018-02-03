#!/usr/bin/perl
use Modern::Perl;
use HTTP::Request::JSON;
use LWP::UserAgent::JSON;
my $request = HTTP::Request::JSON->new(%s,
"POST") https://www.directfreight.com/api/postings/%7Bposting_type%7D
$request->content('{"comment":{},"custom_id":{},"destination_city":{},"destination_state":{},"height":{},"length":{},"load_size":{},"origin_city":{},"origin_state":{},"other_trailer_types":{},"pay_rate":{},"posting_id":0,"receive_date":{},"ship_date":{},"trailer_type":{},"weight":{},"width":{}}');
my $browser = LWP::UserAgent::JSON->new();
my $response = $browser->request($request);
print $response->json_content;