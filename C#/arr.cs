using System;
using System.IO;
using System.Linq;

namespace ConsoleApp1
{

    class Program
    {
      
      
        static void Main(string[] args)
        {
            int[] numbers = new int[] { 3,4,6,9,7};
            Console.WriteLine("Length " + numbers.Length);
            Console.WriteLine("index is " + Array.IndexOf(numbers, 9));
           
            //clear method
            Array.Clear(numbers, 0, 2);
            foreach (var n in numbers)
            {
                Console.WriteLine(n);
            }
            //Copy method
            int[] anotherarray = new int[3];
            Array.Copy(numbers, anotherarray, 3);
            Console.WriteLine("Another array: ");
            foreach(var n in anotherarray)
            {

                Console.WriteLine(n);
            }

            //Sort method
            Array.Sort(numbers);
            Console.WriteLine("Sorting");
            foreach(var n in numbers)
            {
                Console.WriteLine(n);
            }

            //Reverse method
            Array.Reverse(numbers);
            Console.WriteLine("Reversed");        
            foreach(var n in numbers)
            {
                Console.WriteLine(n);
            }
        
       
        }
    }
}
