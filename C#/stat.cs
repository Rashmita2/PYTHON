using System;

namespace ConsoleApp1
{
    public class Person
    {
        public string name;
        public void Introduce(string to)
        {
            Console.WriteLine(" Hi {0}, I am {1} ", to, name);
        }
        public static Person Parse(string str)
        {
            var person = new Person();
            person.name = str;
            return person;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
          
            var p = Person.Parse("John");
            p.Introduce("Ryan");
        }
    }
}
