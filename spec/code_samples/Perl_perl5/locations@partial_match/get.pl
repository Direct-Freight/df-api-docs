#!/usr/bin/perl
use Modern::Perl;
use HTTP::Request::JSON;
use LWP::UserAgent::JSON;
my $request = HTTP::Request::JSON->new(GET,
"'https://www.directfreight.com/api/locations/partial_match?term=SOME_STRING_VALUE&search_type=SOME_STRING_VALUE'")
my $browser = LWP::UserAgent::JSON->new();
my $response = $browser->request($request);
print $response->json_content;