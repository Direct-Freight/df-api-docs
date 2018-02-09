#!/usr/bin/perl
use Modern::Perl;
use Data::Dumper;
use HTTP::Request::JSON;
use LWP::UserAgent::JSON;
my $request = HTTP::Request::JSON->new("POST",
"https://www.directfreight.com/api/boards/hidden_companies");
$request->content('{"company_name":"<ADD STRING VALUE>"}');
my $browser = LWP::UserAgent::JSON->new();
my $response = $browser->request($request);
print Dumper($response->json_content);