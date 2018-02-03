#!/usr/bin/perl
use Modern::Perl;
use Data::Dumper;
use HTTP::Request::JSON;
use LWP::UserAgent::JSON;
my $request = HTTP::Request::JSON->new("PATCH",
"https://www.directfreight.com/api/boards/hidden_entries");
$request->content('{"entry_id":["<ADD STRING VALUE>"]}');
my $browser = LWP::UserAgent::JSON->new();
my $response = $browser->request($request);
print Dumper($response->json_content);