#!/usr/bin/perl
use Modern::Perl;
use HTTP::Request::JSON;
use LWP::UserAgent::JSON;
my $request = HTTP::Request::JSON->new(%s,
"GET") 'https://www.directfreight.com/api/locations/closest_city?latitude=SOME_NUMBER_VALUE&longitude=SOME_NUMBER_VALUE'
my $browser = LWP::UserAgent::JSON->new();
my $response = $browser->request($request);
print $response->json_content;