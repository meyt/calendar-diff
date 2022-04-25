using System;
using System.Globalization;

public class Program
{
	public static void Main()
	{
		string GregorianDate = "622-3-22";
		DateTime d = DateTime.Parse(GregorianDate);
		PersianCalendar pc = new PersianCalendar();
		while (true)
		{
		  int year = pc.GetYear(d);
		  int month = pc.GetMonth(d);
		  int day = pc.GetDayOfMonth(d);
		  if (year == 3178) { break; }
		  Console.WriteLine(string.Format("{0}-{1}-{2},{3}-{4}-{5}", d.Year, d.Month, d.Day, pc.GetYear(d), pc.GetMonth(d), pc.GetDayOfMonth(d)));
		  d = d.AddDays(1);
		}
	}
}
