using System;

namespace Startapplication
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello C# Learners");
            //creating an instance of non-static method
            Program p1 = new Program();
            p1.Print();
        }
        //non static method
        void Print()
        {
            Console.WriteLine("This is print method.");
        }
    }
}


