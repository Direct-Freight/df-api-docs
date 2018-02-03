#!/usr/bin/perl
use Modern::Perl;
use HTTP::Request::JSON;
use LWP::UserAgent::JSON;
my $request = HTTP::Request::JSON->new(%s,
"GET") 'https://www.directfreight.com/api/alerts/%7Balert_type%7D?alert_id=SOME_ARRAY_VALUE'
my $browser = LWP::UserAgent::JSON->new();
my $response = $browser->request($request);
print $response->json_content;