# $Id: import.t,v 1.3 2003/06/24 07:16:28 koschei Exp $
use Test::More tests => 8;
use lib 'inc';
use blib;
use vars qw( $class );

BEGIN {
    $class = 'DateTime::Format::Builder';
    use_ok $class;
}

{
    eval q[
	package SampleClass1;
	use DateTime::Format::Builder
	    parsers => {
		parse_datetime => [
		{
		    regex => qr/^(\d{4})(\d\d)(d\d)(\d\d)(\d\d)(\d\d)$/,
		    params => [qw( year month day hour minute second )],
		},
		{
		    regex => qr/^(\d{4})(\d\d)(\d\d)$/,
		    params => [qw( year month day )],
		},
		],
	    };
    ];
    ok( !$@, "No errors when creating the class." );

    my $parser = SampleClass1->new();
    isa_ok( $parser => 'SampleClass1' );

    my $dt = eval { $parser->parse_datetime( "20040506" ) };
    isa_ok( $dt => 'DateTime' );

    is( $dt->year	=> 2004, 'Year is 2004' );
    is( $dt->month	=> 5, 'Year is 2004' );
    is( $dt->day	=> 6, 'Year is 2004' );

    eval { $parser->fnerk };
    ok( $@, "There is no fnerk." );
}

