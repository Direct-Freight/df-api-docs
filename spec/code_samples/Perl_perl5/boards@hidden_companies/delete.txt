#!/usr/bin/perl
use Modern::Perl;
use HTTP::Request::JSON;
use LWP::UserAgent::JSON;
my $request = HTTP::Request::JSON->new(%s,
"DELETE") 'https://www.directfreight.com/api/boards/hidden_companies?company_id=SOME_STRING_VALUE'
my $browser = LWP::UserAgent::JSON->new();
my $response = $browser->request($request);
print $response->json_content;