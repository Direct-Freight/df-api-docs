#!/usr/bin/perl
use Modern::Perl;
use Data::Dumper;
use HTTP::Request::JSON;
use LWP::UserAgent::JSON;
my $request = HTTP::Request::JSON->new("POST",
"https://www.directfreight.com/api/postings/multiple/%7Blist_type%7D");
$request->content('{"contact_fax":"<ADD STRING VALUE>","contact_name":"<ADD STRING VALUE>","contact_phone":"<ADD STRING VALUE>","delete_current_before_posting":false,"list":["<ADD STRING VALUE>"]}');
my $browser = LWP::UserAgent::JSON->new();
my $response = $browser->request($request);
print Dumper($response->json_content);