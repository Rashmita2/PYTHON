using System;
using System.IO;
using System.Linq;

namespace ConsoleApp1
{

    class Program
    {
        public static int Calculatedemerit(int num)
        {
            int dem =  num / 5;
            if(dem > 12)
            {
                Console.WriteLine("License Suspended");
            }
            return dem;
        }
        static void Main(string[] args)
        {
            int speed = 50;
            Console.WriteLine("Enter the speed limit: ");
            int num = Convert.ToInt32(Console.ReadLine());
            if(num < speed)
            {
                Console.WriteLine("OK");
            }
            else if(num > speed)
            {
                int greatervalue = num - speed;
                int a = Calculatedemerit(greatervalue);
                Console.WriteLine("The value is " + a);
            }

        }
    }
}
