using System;

namespace Freecode
{
    class Program
    {
        static void Main(string[] args)
        {
            Greeting("Lance");
            Greeting("Mary");
            
        }
        static void Greeting(string name)
        {
            Console.WriteLine("Good morning " + name);
        }
    }
}
