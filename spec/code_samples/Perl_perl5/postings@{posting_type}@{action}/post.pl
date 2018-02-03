#!/usr/bin/perl
use Modern::Perl;
use HTTP::Request::JSON;
use LWP::UserAgent::JSON;
my $request = HTTP::Request::JSON->new(POST,
"https://www.directfreight.com/api/postings/%7Bposting_type%7D/%7Baction%7D")
$request->content('{"source_id":{},"source_posting":"<ADD STRING VALUE>"}');
my $browser = LWP::UserAgent::JSON->new();
my $response = $browser->request($request);
print $response->json_content;