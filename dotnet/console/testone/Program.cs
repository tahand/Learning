
Console.WriteLine("Hello, World!");

System.Console.WriteLine("This is a test program.");
System.Console.WriteLine("Andrew");

// this is ran as a top level application meaning that the compilers creates the class that would normally be there with the main method and adds this to the class.

string one = new string("Hello world");
var two = "another way to write strings";
string three = new("and another way");

Console.WriteLine(one);
Console.WriteLine(two);
Console.WriteLine(three);


Console.WriteLine("Listing the arguements....");

foreach (var arg in args)
{
    Console.WriteLine(arg);
}

// if using a class for the args then the args needs to be declared as a string array
// eg static void Main(string[] args)

int x = 30;
int y = 20;

Console.WriteLine(x + "::" + y);

for (int i = 0; i < 10; i++)
{
    Console.WriteLine(i);
}

for (int i = 9; i >= 0; i--)
{
    Console.WriteLine(i);
}

const int a = 100;
Console.WriteLine(a);

method();
///methods can be declared before or after they are called.
/// 
/// 
void method()
{
    Console.WriteLine("this is a method");
}



