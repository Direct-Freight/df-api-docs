#!/usr/bin/perl
use Modern::Perl;
use Data::Dumper;
use HTTP::Request::JSON;
use LWP::UserAgent::JSON;
my $request = HTTP::Request::JSON->new("PATCH",
"https://www.directfreight.com/api/boards/notes");
$request->content('{"body":"<ADD STRING VALUE>","title":"<ADD STRING VALUE>"}');
my $browser = LWP::UserAgent::JSON->new();
my $response = $browser->request($request);
print Dumper($response->json_content);